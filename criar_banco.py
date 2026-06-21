<<<<<<< HEAD
import sqlite3

conn = sqlite3.connect("bancodados.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS notas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    matematica TEXT NOT NULL,
    ciencias TEXT NOT NULL,
    portugues TEXT NOT NULL,
    artes TEXT NOT NULL,
    geografia TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL
)
""")

conn.commit()
=======
import sqlite3

conn = sqlite3.connect("bancodados.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS notas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    matematica TEXT NOT NULL,
    ciencias TEXT NOT NULL,
    portugues TEXT NOT NULL,
    artes TEXT NOT NULL,
    geografia TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL
)
""")

conn.commit()
>>>>>>> 0bce4efb631d0b67677c253602ab2102c7bc63ef
conn.close()