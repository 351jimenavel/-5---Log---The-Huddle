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

#print(logs_autenticacion)

### Asi funciona datetime 
#hoy = datetime.now()
#print(f"Hoy es {hoy.day}/{hoy.month}/{hoy.year}. Son las {hoy.hour}:{hoy.minute}:{hoy.second}")

## Mismo ejercicio pero mas dinamico y utilizando datetime.

# Para hacerlo mas dinamico: 
## (a) Continuamos con la aleatoriedad en los log levels.
log_levels = ["INFO", "WARNING", "ERROR", "DEBUG", "CRITICAL"]

## (b) Aleatoriedad en los mensajes
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
    #print(log)

print(logs_autenticacion)