"""
1- Archivo Generador de Base de Datos para el challenge de Logging Distribuido.
"""
import sqlite3
from config import DB_PATH

def iniciar_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            service TEXT NOT NULL, 
            severity TEXT NOT NULL, 
            message TEXT NOT NULL,
            received_at TEXT NOT NULL
        )""")

        conn.commit()

if __name__ == "__main__":
    iniciar_db()
    print("Seeder OK. DB en:", DB_PATH)