'''
2- Archivo Servidor central de Logging Distribuido (Flask + SQLite).

Responsabilidades:
- GET /logs: devolver logs filtrados por query params (service, severity).
- POST /logs: validar token, validar/normalizar payload, persistir en SQLite y responder 201.
'''

# importamos dependencias
from flask import Flask, request, jsonify       # crea la app. lee lo que llega en la HTTP (headers, query params, body). arma respuestas JSON correctas.
from datetime import datetime, timezone
import sqlite3
from pathlib import Path
from config import DB_PATH

app = Flask(__name__)   

TOKEN_VALIDOS = {"ABC123": "Frontend", "DEF456": "AuthService"}

@app.route("/")
def inicio():
    """Healthcheck simple para saber que el server vive."""
    print("[SERVER] Iniciando server...")
    return jsonify({"status":"ok"}), 200

@app.route("/logs", methods=["GET","POST"])
def recibir_logs():

    # Logica de metodo GET - filtros opcionales 
    if request.method == "GET":

        # Query params -> /logs?service=AuthService&severity=ERROR
        args = request.args
        print(args)
        service = args.get("service")
        severity = args.get("severity")

        query = "SELECT * FROM logs WHERE 1=1 "
        condiciones = []    # lista de condiciones (sintaxis)
        parametros = []    # lista de filtros que den true

        if service:
            condiciones.append("service = ?")
            parametros.append(service)

        if severity:
            condiciones.append("severity = ?")
            parametros.append(severity.upper())

        if condiciones:
            # antes: query += " WHERE " + " AND ".join(condiciones)
            # ya tenemos "WHERE 1=1 " arriba, acá solo sumamos los AND
            query += " AND " + " AND ".join(condiciones)
        
        query += " ORDER BY received_at DESC"
        # query += " ORDER BY id ASC"

        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row       # row_factory permite convertir filas a dict fácilmente.
            cur  = conn.execute(query, parametros)
            rows = cur.fetchall()

        # Serializamos filas a lista de dicts apta para jsonify
        response = []
        for r in rows:
            response.append(dict(r))
        
        return jsonify({"data": response}), 200
    
    # Logica de metodo POST
    if request.method == "POST":

        ''' 
        1. VALIDACIONES/NORMALIZACIONES 
        '''
        # 1.1) Autenticacion
        auth = request.headers.get("Authorization", "")
        prefijo = "Token "
        if not auth or not auth.startswith(prefijo):
            return jsonify({"error":"Cliente desconocido"}), 401    # Unauthorized

        # 1.2) Tipo de contenido correcto 
        # Chequeo de header
        if not request.is_json:
            return jsonify({"error":"Content-Type debe ser application/json"}), 415     # Unsupported MediaType
        
        # Parseo seguro del cuerpo JSON
        # get_json is used to parse incoming JSON request data and convert it into a Python dictionary.
        data = request.get_json(silent=True)    # Intenta parsear JSON, retornara None si es invalido
        if data is None:
            return jsonify({"error":"json inválido"}), 400      # Bad Request
        
        # 1.3) Campos obligatorios
        campos_obligatorios = ["timestamp","service","severity","message"]
        for campo in campos_obligatorios:
            if campo not in data:
                return jsonify({"error":f"campo {campo} requerido"}), 400
        
        # 1.4) Relacion token y servicios
        token_solito = auth[len(prefijo):].strip()
        service_from_token = TOKEN_VALIDOS.get(token_solito)
        if not service_from_token or data["service"] != service_from_token:
            return jsonify({"error":"Quien sos, bro?"}), 401
        
        # 1.5) Severity 
        severidades_permitidas = {"INFO","DEBUG","WARN","ERROR"}
        if data["severity"] not in severidades_permitidas:
            return jsonify({"error":"severity invalido"}), 400
        
        # 1.6) Timestamp ISO con zona - parseo + normalización a UTC
        ts_extraido = str(data["timestamp"])
        ts_normalizado = ts_extraido.strip().replace(" ", "T").replace("Z", "+00:00")
        try:
            datetime_evento = datetime.fromisoformat(ts_normalizado)
        except Exception:
            return jsonify({"error":"timestamp inválido (use ISO 8601)"}), 400

        if datetime_evento.tzinfo is None:
            return jsonify({"error":"timestamp sin zona horaria"}), 400

        ''' 
        2) Sellos de tiempo consistentes en UTC
        '''
        # received at
        received_at = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")

        # timestamp
        ts = datetime_evento.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")

        '''
        3) Logica DB
        '''
        # Poblacion
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cur = conn.execute(
                    "INSERT INTO logs (timestamp, service, severity, message, received_at) VALUES (?,?,?,?,?)",
                    (ts, data["service"], data["severity"], data["message"], received_at)
                )
                log_id = cur.lastrowid
        except Exception as e:
            print("DB ERROR:", repr(e))
            return jsonify({"error": "db error"}), 500

        '''
        4) Generar respuesta
        '''
        return jsonify({
            "status":"ok",
            "id":log_id,
            "received_at":received_at,
            "log":{
                "timestamp": ts, 
                "service": data["service"], 
                "severity": data["severity"], 
                "message":data["message"]}
        }), 201     # Created
    
            
if __name__ == "__main__":
    app.run(debug=True, port=8000)