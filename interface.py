import tkinter as tk
from tkinter import messagebox
from livro import Livro
import cadastro

livro_selecionado = None

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
        limpar_campos_entrada()

def atualizar_lista():
    lista.delete(0, tk.END)
    for l in cadastro.listar_livros():
        lista.insert(tk.END, str(l))

def limpar_campos_entrada():
    for entry in [titulo_entry, autor_entry, ano_entry, isbn_entry, nome_locatario_entry]:
        entry.delete(0, tk.END)
    alugado_var.set(False)
    nome_locatario_entry.config(state="disabled")

def confirmar_limpar_todos_livros():
    if messagebox.askyesno("Confirmar Limpeza", "Tem certeza que deseja apagar TODOS os livros registrados?"):
        cadastro.remover_todos_livros()
        atualizar_lista()
        limpar_campos_entrada()
        messagebox.showinfo("Limpeza concluída", "Todos os livros foram apagados.")

def buscar():
    lista.delete(0, tk.END)
    titulo = titulo_entry.get()
    autor = autor_entry.get()
    ano = ano_entry.get()
    isbn = isbn_entry.get()

    resultados = cadastro.buscar_livro(titulo=titulo, autor=autor, ano=ano, isbn=isbn)
    for l in resultados:
        lista.insert(tk.END, str(l))

def remover():
    cadastro.remover_livro(titulo_entry.get())
    atualizar_lista()

def preencher_campos():
    global livro_selecionado
    if not lista.curselection():
        return
    index = lista.curselection()[0]
    livro = cadastro.listar_livros()[index]
    livro_selecionado = livro.titulo

    titulo_entry.delete(0, tk.END)
    titulo_entry.insert(tk.END, livro.titulo)

    autor_entry.delete(0, tk.END)
    autor_entry.insert(tk.END, livro.autor)

    ano_entry.delete(0, tk.END)
    ano_entry.insert(tk.END, livro.ano)

    isbn_entry.delete(0, tk.END)
    isbn_entry.insert(tk.END, livro.isbn)

    alugado_var.set(livro.status == "alugado")
    nome_locatario_entry.config(state="normal" if alugado_var.get() else "disabled")
    nome_locatario_entry.delete(0, tk.END)
    nome_locatario_entry.insert(tk.END, livro.nome_locatario)

def atualizar():
    if not livro_selecionado:
        messagebox.showwarning("Aviso", "Selecione um livro na lista para atualizar.")
        return

    novo_titulo = titulo_entry.get()
    novo_autor = autor_entry.get()
    novo_ano = ano_entry.get()
    novo_isbn = isbn_entry.get()
    alugado = alugado_var.get()
    novo_nome_locatario = nome_locatario_entry.get() if alugado else ""
    novo_status = "alugado" if alugado else "disponível"

    livro_novo = Livro(novo_titulo, novo_autor, novo_ano, novo_isbn, novo_status, novo_nome_locatario)
    cadastro.atualizar_livro(livro_selecionado, livro_novo)
    atualizar_lista()
    limpar_campos_entrada()

def confirmar_saida():
    if messagebox.askokcancel("Sair", "Deseja realmente sair?"):
        root.destroy()

def iniciar_interface():
    global titulo_entry, autor_entry, ano_entry, isbn_entry, lista
    global alugado_var, nome_locatario_entry, root

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
    tk.Button(root, text="Atualizar", command=atualizar).grid(row=6, column=2)
    tk.Button(root, text="Remover", command=remover).grid(row=7, column=0)
    tk.Button(root, text="Limpar Tudo", command=confirmar_limpar_todos_livros).grid(row=7, column=1)
    tk.Button(root, text="Sair", command=confirmar_saida).grid(row=7, column=2)

    # Lista
    lista = tk.Listbox(root, width=60)
    lista.grid(row=8, column=0, columnspan=3)
    lista.bind('<<ListboxSelect>>', lambda e: preencher_campos())

    atualizar_lista()
    root.mainloop()

# Iniciar a interface ao rodar o script
iniciar_interface()
