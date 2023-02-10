import sqlite3

conexao = sqlite3.connect("Sistema.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    confirmpassword TEXT NOT NULL
);
""")

print("Conectado ao Banco de Dados!")
