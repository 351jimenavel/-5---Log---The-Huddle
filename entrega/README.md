# 🐧 Logging Distribuido – Flask + SQLite

Servicio central de **logging distribuido**. Recibe logs por HTTP desde múltiples servicios, los **valida**, **normaliza** (fechas en UTC) y los **guarda** en SQLite. Permite consultarlos con **filtros por query params**.

---

## ✨ Features

- **POST /logs**: recibe logs en JSON, con **autenticación por token**.
- **Validaciones**: 'Content-Type', JSON, campos obligatorios, 'severity' (INFO/DEBUG/WARN/ERROR), 'timestamp' ISO8601 con zona.
- **Normalización de tiempo**: convierte 'timestamp' del evento a **UTC (Z)** y genera 'received_at' (cuándo llegó al server).
- **GET /logs**: consulta con filtros por 'service' y 'severity'.
- **SQLite** persistente (archivo 'logs.db').

---

## 🧱 Arquitectura (simple y directa)

- **Server**: 'Flask' expone '/logs' (GET/POST).
- **DB**: 'SQLite' con tabla 'logs(id, timestamp, service, severity, message, received_at)'.
- **Clientes simulados**: 'client.py' genera y envía logs de 'Frontend' y 'AuthService' con su **token** correspondiente.

---

## 📂 Estructura sugerida
```
carpeta/
├─ main.py            # Servidor Flask (endpoints, validaciones, persistencia)
├─ client.py          # Cliente simulador (envía logs con tokens)
├─ seeder.py          # Crea tabla 'logs' en logs.db
├─ config.py          # DB_PATH usando pathlib (ruta absoluta y portable)
├─ tests.http         # Suite de pruebas manuales (REST Client VS Code)
├─ requirements.txt
└─ logs.db            # (creado por seeder.py)
```

## 🚀 Quickstart

> Orden recomendado: **seeder → server → cliente**  
> Motivo: el **seeder** crea la tabla 'logs' en SQLite antes de que el server reciba inserts.

### 1- Requisitos
- Python **3.10+** (probado con 3.11)
- pip
- (Opcional) VS Code + extensión **REST Client** para 'tests.http'

### 2- Crear entorno e instalar dependencias

**Windows (PowerShell)**
```powershell
py -m venv .venv
. .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Linux / macOS**
```powershell
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
### 3- Crear la base (Seeder)
Crea (si no existe) el archivo logs.db y la tabla logs.
```powershell
python seeder.py
```
### 4- Levantar el servidor
Servirá en http://127.0.0.1:8000
```powershell
python main.py
```
### 5- Enviar logs (cliente simulado)
El cliente envía N logs alternando servicios y severidades, usando los tokens configurados.
```powershell
# En otra terminal (con el venv activado):
python client.py

```
### 6- Filtros por Query Params (GET /logs)

**Endpoint:** 'GET /logs'  
**Todos los filtros son opcionales.** Si no mandás nada, devuelve todos los logs.

### Parámetros soportados (hoy)
- 'service' → nombre exacto del servicio ('Frontend' | 'AuthService')
- 'severity' → nivel del log ('INFO' | 'DEBUG' | 'WARN' | 'ERROR')  
  > Es **case-insensitive** en la query ('error', 'Error', 'ERROR' -> todos valen).

### 7- Pruebas manuales
VS Code REST Client
Abrí tests.http y clic en “Send Request” en cada caso (espera: 201/401/415/400).

### 8- Guia de Codigos HTTP
```
200  OK
201  Created
400  Bad Request
401  Unauthorized
415  Unsupported Media Type
500  Internal Server Error
```