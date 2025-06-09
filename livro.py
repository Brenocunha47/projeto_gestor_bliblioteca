class Livro:
    def __init__(self, titulo, autor, ano, isbn, status, nome_locatario=""):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.isbn = isbn
        self.status = status
        self.nome_locatario = nome_locatario

    def __str__(self):
        if self.status == "alugado":
            return f"{self.titulo} - {self.autor} ({self.ano}) | ISBN: {self.isbn} | {self.status} por {self.nome_locatario}"
        else:
            return f"{self.titulo} - {self.autor} ({self.ano}) | ISBN: {self.isbn} | {self.status}"
