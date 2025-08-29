"""
3- Archivo Cliente simulador de logs para el challenge de Logging Distribuido.
"""

import requests
from datetime import datetime, timezone
import time
import random

# Endpoint del servidor central
URL = "http://127.0.0.1:8000/logs"

# Tokens validos por servicio (deben coincidir con el whitelist del servidor)
# Importante: este dict define la identidad del cliente para cada "service".
TOKENS = {"Frontend": "ABC123", "AuthService": "DEF456"}

# Conjunto acotado de severidades
SEVERITIES = ["INFO","DEBUG","WARN","ERROR"]

# Mensajes “creibles” para poblar los logs de prueba
MESSAGES = [
    "Nuevo usuario ha iniciado sesion",
    "Intento de login fallido (usuario inexistente)",
    "Token invalido recibido",
    "Chequeando credenciales del usuario",
    "Servicio caido"
]

# Lista de servicios simulados (coinciden con las claves de TOKENS)
SERVICES = [
    "Frontend",
    "AuthService"
]

def now_iso_utc():
    """
    Devuelve el instante actual en ISO 8601, en UTC y con precisión al segundo.
    Ejemplo: '2025-08-28T15:34:56Z'
    Por que UTC: facilita ordenar/filtrar por texto en la base y evita ambigüedades de zona horaria.
    """
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")  # zulu time -  otra manera de decir UTC

def generar_log(servicio):
    """
    Construye un dict con la forma exacta que espera el servidor
    """
    return {
        "timestamp": now_iso_utc(),
        "service": servicio,
        "severity": random.choice(SEVERITIES),
        "message": random.choice(MESSAGES)
    }

def enviar(log):
    """
    Envía un log al servidor central
    """
    token = TOKENS[log["service"]]
    r = requests.post(URL, json=log, headers={
        #"Content-Type": "application/json",
        "Authorization": f"Token {token}"
    }, timeout=5)
    print(r.status_code, r.text)
    return r

if __name__ == "__main__":

    N = 10
    # simula cantidad N de logs
    for i in range(N):           
        # Se elige un servicio al azar y se genera un log
        service = random.choice(SERVICES)
        log = generar_log(service)
        print(f"Log enviado: {log}")

        # Enviamos y manejamos error de forma básica
        try:
            enviar(log)
        except requests.RequestException as e:
            print(f"Error de red: {e}")

        time.sleep(1)
