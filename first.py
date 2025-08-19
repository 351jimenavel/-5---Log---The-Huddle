'''Archivo de practica'''
# 1. Escribir los primeros logs en JSON a mano (copiar ejemplos, inventar).

logs_autenticacion = [
{
    "timestamp" : "2023-06-16 14:30:22",
    "severity" : "INFO",
    "service" : "AuthService",
    "message" : "Nuevo usuario ha iniciado sesion"
},
{
    "timestamp" : "2024-02-16 14:30:22",
    "severity" : "WARNING",
    "service" : "AuthService",
    "message" : "Intento de login fallido (usuario inexistente)"
},
{
    "timestamp" : "2025-04-16 14:30:22",
    "severity" : "ERROR",
    "service" : "AuthService",
    "message" : "Token inválido recibido"
},
{
    "timestamp" : "2025-04-16 14:30:22",
    "severity" : "DEBUG",
    "service" : "AuthService",
    "message" : "Chequeando credenciales del usuario"
},
{
    "timestamp" : "2025-04-16 14:30:22",
    "severity" : "CRITICAL",
    "service" : "AuthService",
    "message" : "Servicio AuthService caído"
}
]

# 2. Crear un script Python que genere logs falsos con random y datetime.

import random
from datetime import datetime
import time

# Otra forma

fechas_random = ["2025-04-16 14:30:22", "2023-06-16 14:30:22", "2024-02-16 14:30:22"]
log_levels = ["INFO", "WARNING", "ERROR", "DEBUG", "CRITICAL"]

logs_autenticacion = [
{
    "timestamp" : random.choice(fechas_random),
    "severity" : random.choice(log_levels),
    "service" : "AuthService",
    "message" : "Nuevo usuario ha iniciado sesion"
},
{
    "timestamp" : random.choice(fechas_random),
    "severity" : random.choice(log_levels),
    "service" : "AuthService",
    "message" : "Intento de login fallido (usuario inexistente)"
},
{
    "timestamp" : random.choice(fechas_random),
    "severity" : random.choice(log_levels),
    "service" : "AuthService",
    "message" : "Token inválido recibido"
},
{
    "timestamp" : random.choice(fechas_random),
    "severity" : random.choice(log_levels),
    "service" : "AuthService",
    "message" : "Chequeando credenciales del usuario"
},
{
    "timestamp" : random.choice(fechas_random),
    "severity" : random.choice(log_levels),
    "service" : "AuthService",
    "message" : "Servicio AuthService caído"
}
]

print(logs_autenticacion)
### Asi funciona datetime 
hoy = datetime.now()
#print(f"Hoy es {hoy.day}/{hoy.month}/{hoy.year}. Son las {hoy.hour}:{hoy.minute}:{hoy.second}")
