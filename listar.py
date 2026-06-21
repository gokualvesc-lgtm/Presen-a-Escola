<<<<<<< HEAD
import sqlite3
import os

print("Banco usado:", os.path.abspath("bancodados.db"))

conn = sqlite3.connect("bancodados.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()
for usuario in usuarios:
    print(usuario)

=======
import sqlite3
import os

print("Banco usado:", os.path.abspath("bancodados.db"))

conn = sqlite3.connect("bancodados.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()
for usuario in usuarios:
    print(usuario)

>>>>>>> 0bce4efb631d0b67677c253602ab2102c7bc63ef
conn.close()