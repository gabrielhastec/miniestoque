import sqlite3
import os

# Caminho absoluto para o banco dentro da pasta database
DB_PATH = os.path.join(os.path.dirname(__file__), "estoque.db")

def get_connection():
    return sqlite3.connect(DB_PATH)
