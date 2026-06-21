import sqlite3
import random

conn = sqlite3.connect("bancodados.db")
cursor = conn.cursor()

# Pega todos os usuários
cursor.execute("SELECT nome FROM usuarios")
usuarios = cursor.fetchall()
cursor.execute("DELETE FROM notas")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='notas'")

for usuario in usuarios:
    nome = usuario[0]

    matematica = str(round(random.uniform(0, 10), 1))
    ciencias = str(round(random.uniform(0, 10), 1))
    portugues = str(round(random.uniform(0, 10), 1))
    artes = str(round(random.uniform(0, 10), 1))
    geografia = str(round(random.uniform(0, 10), 1))

    cursor.execute("""
        INSERT INTO notas (
            nome,
            matematica,
            ciencias,
            portugues,
            artes,
            geografia
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        nome,
        matematica,
        ciencias,
        portugues,
        artes,
        geografia
    ))

conn.commit()
conn.close()

print("Notas geradas!")