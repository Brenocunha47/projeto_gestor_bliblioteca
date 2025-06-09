import sqlite3
from livro import Livro

# Criação e conexão com o banco de dados
conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

# Cria a tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        autor TEXT,
        ano TEXT,
        isbn TEXT,
        status TEXT,
        nome_locatario TEXT
    )
''')
conn.commit()

def adicionar_livro(livro):
    cursor.execute('''
        INSERT INTO livros (titulo, autor, ano, isbn, status, nome_locatario)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (livro.titulo, livro.autor, livro.ano, livro.isbn, livro.status, livro.nome_locatario))
    conn.commit()

def listar_livros():
    cursor.execute('SELECT titulo, autor, ano, isbn, status, nome_locatario FROM livros')
    rows = cursor.fetchall()
    return [Livro(*row) for row in rows]

# 🔍 NOVA versão da função buscar_livro
def buscar_livro(titulo="", autor="", ano="", isbn=""):
    query = '''
        SELECT titulo, autor, ano, isbn, status, nome_locatario FROM livros WHERE 1=1
    '''
    params = []

    if titulo:
        query += " AND titulo LIKE ?"
        params.append(f"%{titulo}%")
    if autor:
        query += " AND autor LIKE ?"
        params.append(f"%{autor}%")
    if ano:
        query += " AND ano LIKE ?"
        params.append(f"%{ano}%")
    if isbn:
        query += " AND isbn LIKE ?"
        params.append(f"%{isbn}%")

    cursor.execute(query, params)
    rows = cursor.fetchall()
    return [Livro(*row) for row in rows]

def remover_livro(titulo):
    cursor.execute('DELETE FROM livros WHERE titulo = ?', (titulo,))
    conn.commit()

def atualizar_livro(titulo_antigo, livro_novo):
    cursor.execute('''
        UPDATE livros SET 
            titulo = ?, 
            autor = ?, 
            ano = ?, 
            isbn = ?, 
            status = ?, 
            nome_locatario = ?
        WHERE titulo = ?
    ''', (livro_novo.titulo, livro_novo.autor, livro_novo.ano,
          livro_novo.isbn, livro_novo.status, livro_novo.nome_locatario,
          titulo_antigo))
    conn.commit()
def remover_todos_livros():
    cursor.execute('DELETE FROM livros')
    conn.commit()
