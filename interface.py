import tkinter as tk
from tkinter import messagebox
from livro import Livro
import cadastro

def adicionar():
    titulo = titulo_entry.get()
    autor = autor_entry.get()
    ano = ano_entry.get()
    isbn = isbn_entry.get()
    alugado = alugado_var.get()
    nome_locatario = nome_locatario_entry.get() if alugado else ""
    status = "alugado" if alugado else "disponível"

    if titulo:
        livro = Livro(titulo, autor, ano, isbn, status, nome_locatario)
        cadastro.adicionar_livro(livro)
        atualizar_lista()
        limpar_campos()

def atualizar_lista():
    lista.delete(0, tk.END)
    for l in cadastro.listar_livros():
        lista.insert(tk.END, str(l))

def limpar_campos():
    for entry in [titulo_entry, autor_entry, ano_entry, isbn_entry, nome_locatario_entry]:
        entry.delete(0, tk.END)
    alugado_var.set(False)
    nome_locatario_entry.config(state="disabled")

def buscar():
    lista.delete(0, tk.END)
    resultados = cadastro.buscar_livro(titulo_entry.get())
    for l in resultados:
        lista.insert(tk.END, str(l))

def remover():
    cadastro.remover_livro(titulo_entry.get())
    atualizar_lista()

def iniciar_interface():
    global titulo_entry, autor_entry, ano_entry, isbn_entry, lista
    global alugado_var, nome_locatario_entry

    root = tk.Tk()
    root.title("Gestor de Biblioteca")

    # Labels
    tk.Label(root, text="Título").grid(row=0, column=0)
    tk.Label(root, text="Autor").grid(row=1, column=0)
    tk.Label(root, text="Ano").grid(row=2, column=0)
    tk.Label(root, text="ISBN").grid(row=3, column=0)
    tk.Label(root, text="Alugado?").grid(row=4, column=0)
    tk.Label(root, text="Nome do locatário").grid(row=5, column=0)

    # Entradas
    titulo_entry = tk.Entry(root)
    autor_entry = tk.Entry(root)
    ano_entry = tk.Entry(root)
    isbn_entry = tk.Entry(root)
    alugado_var = tk.BooleanVar()
    nome_locatario_entry = tk.Entry(root, state="disabled")

    titulo_entry.grid(row=0, column=1)
    autor_entry.grid(row=1, column=1)
    ano_entry.grid(row=2, column=1)
    isbn_entry.grid(row=3, column=1)

    tk.Checkbutton(root, variable=alugado_var,
                   command=lambda: nome_locatario_entry.config(
                       state="normal" if alugado_var.get() else "disabled")
                   ).grid(row=4, column=1)

    nome_locatario_entry.grid(row=5, column=1)

    # Botões
    tk.Button(root, text="Adicionar", command=adicionar).grid(row=6, column=0)
    tk.Button(root, text="Buscar", command=buscar).grid(row=6, column=1)
    tk.Button(root, text="Remover", command=remover).grid(row=7, column=0)
    tk.Button(root, text="Limpar", command=limpar_campos).grid(row=7, column=1)

    # Lista
    lista = tk.Listbox(root, width=60)
    lista.grid(row=8, column=0, columnspan=2)

    atualizar_lista()
    root.mainloop()
