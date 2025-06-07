livros = []

def adicionar_livro(livro):
    livros.append(livro)

def listar_livros():
    return livros

def buscar_livro(titulo):
    return [l for l in livros if titulo.lower() in l.titulo.lower()]

def remover_livro(titulo):
    global livros
    livros = [l for l in livros if titulo.lower() not in l.titulo.lower()]
