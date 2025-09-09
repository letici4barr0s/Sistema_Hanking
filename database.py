import sqlite3

DB_NAME = "jogadores.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def criar_tabela():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS jogadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            nivel INTEGER NOT NULL,
            pontuacao REAL NOT NULL,
            lista INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def inserir_jogador(nome, nivel, pontuacao, lista):
    conn = conectar()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO jogadores (nome, nivel, pontuacao, lista) VALUES (?, ?, ?, ?)",
        (nome, nivel, pontuacao, lista)
    )
    conn.commit()
    conn.close()

def buscar_listas():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT lista FROM jogadores ORDER BY lista")
    listas = [row[0] for row in cur.fetchall()]
    conn.close()
    return listas

def buscar_por_lista(lista):
    conn = conectar()
    cur = conn.cursor()
    cur.execute(
        "SELECT nome, nivel, pontuacao FROM jogadores WHERE lista = ? ORDER BY pontuacao DESC",
        (lista,)
    )
    jogadores = cur.fetchall()
    conn.close()
    return jogadores
