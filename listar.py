import sqlite3
import os

print("Banco usado:", os.path.abspath("bancodados.db"))

conn = sqlite3.connect("bancodados.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()
for usuario in usuarios:
    print(usuario)

conn.close()