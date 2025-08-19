# Teniendo los logs simulados del archivo 1-first, pasamos a la siguiente practica: Enviar logs a un endpoint de prueba
import random
from datetime import datetime
import time
import requests
import json

# ----------------------- (1) Generar Logs -----------------------
log_levels = ["INFO", "WARNING", "ERROR", "DEBUG", "CRITICAL"]
mensajes = [
    "Nuevo usuario ha iniciado sesión",
    "Intento de login fallido (usuario inexistente)",
    "Token inválido recibido",
    "Chequeando credenciales del usuario",
    "Servicio AuthService caído"
]

logs_autenticacion = [] # aqui se agregaran los logs

for _ in range(5):  # Generamos 5 logs falsos
    # estructura que tendra cada log
    log = {
    ## (c) Usar datetime.now    
        "timestamp" : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),    # con su string format time para pasarle un formato exacto (year-month-day hour-minute-second sin microseg)
        "severity" : random.choice(log_levels),
        "service" : "AuthService",
        "message" : random.choice(mensajes)
    }
    logs_autenticacion.append(log)   # anhadimos los logs generados 

    ## (d) timesleep para simular que pasa x tiempo entre cada log
    time.sleep(2)

# Ejercicio 1: mandar un JSON a httpbin.org/post
with open('log.json', "w", encoding="utf-8") as f:
    json.dump(logs_autenticacion, f, ensure_ascii=False, indent=2)

with open('log.json', 'r', encoding='utf-8') as f:
    datos = json.load(f)

# ----------------------- (2) Enviar a httpbin (simple) -----------------------
# Endpoint de prueba: https://httpbin.org/post
ENDPOINT = 'https://httpbin.org/post'
r = requests.post(ENDPOINT, json=datos)
# print(r.status_code)      # código HTTP (200 si todo bien)
# print(r.json())           # la respuesta completa que devuelve httpbin

# ----------------------- (3) Enviar con header y validar formato del token -----------------------
headers = {"Authorization": "Token ABC123"}
r = requests.post(ENDPOINT, json=datos, headers=headers, timeout=3)
print(r.status_code)      # código HTTP (200 si todo bien)
print(r.json()["headers"])           # la respuesta completa que devuelve httpbin

eco = r.json()
print("HTTP:", r.status_code)               # 200
print("Auth visto:", eco['headers'].get('Authorization'))  # "Token ABC123"

# Validacion
auth_val = eco['headers'].get('Authorization')
if not auth_val.startswith('Token '):
    print('Falta prefijo "Token "')
else:
    print("Header Authorization con formato correcto")
