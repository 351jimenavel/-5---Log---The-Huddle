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

# 🐧 Distributed Logging – Flask + SQLite

Central **distributed logging** service. It receives logs over HTTP from multiple services, **validates** them, **normalizes** timestamps to UTC, and **stores** everything in SQLite. You can query logs using **URL query params**.

---

## ✨ Features

- **POST `/logs`**: receive logs in JSON with **token-based authentication**.
- **Validations**: `Content-Type`, JSON well-formed, required fields, `severity` (`INFO`/`DEBUG`/`WARN`/`ERROR`), and ISO-8601 `timestamp` **with timezone**.
- **Time normalization**: converts event `timestamp` to **UTC (`Z`)** and generates `received_at` (when the server received it).
- **GET `/logs`**: query with filters by `service` and `severity`.
- **SQLite** persistence (`logs.db` file).

---

## 🧱 Architecture (simple & direct)

- **Server**: `Flask` exposes `/logs` (GET/POST).
- **DB**: `SQLite` table `logs(id, timestamp, service, severity, message, received_at)`.
- **Simulated clients**: `client.py` generates and sends logs for `Frontend` and `AuthService` using their **tokens**.

---

## 📂 Suggested Structure
```text
entrega/
├─ main.py            # Flask server (endpoints, validations, persistence)
├─ client.py          # Log simulator (sends logs with tokens)
├─ seeder.py          # Creates table 'logs' in logs.db
├─ config.py          # DB_PATH via pathlib (absolute & portable)
├─ tests.http         # Manual test suite (VS Code REST Client)
├─ requirements.txt
└─ logs.db            # (created by seeder.py)
```

---
## 🚀 Quickstart

> Recommended order: **seeder → server → client**  
> Why: the **seeder** creates the `logs` table in SQLite before inserts.

### 1) Requirements
- Python **3.10+** (tested with 3.11)
- `pip`
- *(Optional)* VS Code + **REST Client** extension for `tests.http`

### 2) Create virtual env & install deps

**Windows (PowerShell)**
```powershell
py -m venv .venv
. .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Linux / macOS**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
### 3) Create the database (Seeder)

Creates `logs.db` (if missing) and the `logs` table.

```bash
python seeder.py
```

### 4) Run the server
Serves at `http://127.0.0.1:8000`

```bash
python main.py
```

### 5) Send logs (simulated client)
Sends N logs alternating services and severities using the configured tokens.

```bash
# In another terminal (with the venv activated):
python client.py
```

### 6) 🔎 Query Param Filters (GET `/logs`)

**Endpoint:** `GET /logs`  
**All filters are optional.** If you don’t send any, it returns all logs.

### Supported parameters (today)
- `service` → exact service name (`Frontend` | `AuthService`)
- `severity` → log level (`INFO` | `DEBUG` | `WARN` | `ERROR`)  
  > **Case-insensitive** in the query (`error`, `Error`, `ERROR` → all work).

### 7) Manual tests (VS Code REST Client)
Open `tests.http` and click **Send Request** on each case (expected: 201/401/415/400).

### 8) HTTP Status Code Guide
```
200  OK
201  Created
400  Bad Request
401  Unauthorized
415  Unsupported Media Type
500  Internal Server Error
```