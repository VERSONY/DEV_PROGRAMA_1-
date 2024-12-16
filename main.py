import tkinter as tk
from tkinter import ttk, messagebox

# Lista de produtos cadastrados
produtos = []

# Função para exibir o formulário de Produto
def exibir_form_produto():
    limpar_tela()
    frame_produto.pack(pady=20)

# Função para exibir o formulário de Cliente
def exibir_form_cliente():
    limpar_tela()
    frame_cliente.pack(pady=20)

# Função para voltar ao menu principal
def voltar_menu():
    limpar_tela()
    botoes_principais.pack(pady=20)

# Função para salvar dados de Produto
def salvar_produto():
    nome = entry_nome_produto.get()
    categoria = entry_categoria_produto.get()
    preco = entry_preco_produto.get()

    if nome and categoria and preco:
        produtos.append((nome, categoria, preco))  # Adiciona o produto à lista
        messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
        limpar_campos_produto()
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

# Função para limpar campos do formulário de Produto
def limpar_campos_produto():
    entry_nome_produto.delete(0, "end")
    entry_categoria_produto.delete(0, "end")
    entry_preco_produto.delete(0, "end")

# Função para limpar tela
def limpar_tela():
    for widget in janela.winfo_children():
        widget.pack_forget()

# Função para exibir a lista de produtos em uma nova janela
def exibir_lista_produtos():
    janela_lista = tk.Toplevel(janela)
    janela_lista.title("Lista de Produtos Cadastrados")
    janela_lista.geometry("400x300")

    # Criação da tabela usando Treeview
    tree = ttk.Treeview(janela_lista, columns=("Nome", "Categoria", "Preço"), show="headings")
    tree.heading("Nome", text="Nome")
    tree.heading("Categoria", text="Categoria")
    tree.heading("Preço", text="Preço")
    tree.pack(fill="both", expand=True)

    # Adicionar os produtos à tabela
    for produto in produtos:
        tree.insert("", "end", values=produto)

# Criação da janela principal
janela = tk.Tk()
janela.title("Menu Principal")
janela.geometry("400x500")
janela.configure(bg="#f8f9fa")

# ------------------ Tela Principal ------------------
botoes_principais = tk.Frame(janela, bg="#f8f9fa")

titulo = tk.Label(botoes_principais, text="Menu Principal", font=("Arial", 24, "bold"), bg="#f8f9fa")
titulo.pack(pady=10)

btn_admin = tk.Button(botoes_principais, text="Admin", bg="#007bff", fg="white", font=("Arial", 12, "bold"), width=20, height=2)
btn_admin.pack(pady=5)

btn_produto = tk.Button(botoes_principais, text="Cadastrar Produto", bg="#28a745", fg="white", font=("Arial", 12, "bold"), width=20, height=2, command=exibir_form_produto)
btn_produto.pack(pady=5)

btn_cliente = tk.Button(botoes_principais, text="Cliente", bg="#c0da16", fg="white", font=("Arial", 12, "bold"), width=20, height=2, command=exibir_form_cliente)
btn_cliente.pack(pady=5)

# Botão para exibir a lista de produtos
btn_lista_produtos = tk.Button(botoes_principais, text="Lista de Produtos", bg="#6c757d", fg="white", font=("Arial", 10), command=exibir_lista_produtos)
btn_lista_produtos.pack(pady=10)

botoes_principais.pack(pady=20)

# ------------------ Formulário de Produto ------------------
frame_produto = tk.Frame(janela, bg="white", padx=20, pady=20, relief="groove", bd=2)

tk.Label(frame_produto, text="Cadastrar Produto", font=("Arial", 16, "bold"), bg="white").pack(pady=5)

tk.Label(frame_produto, text="Nome do Produto:", bg="white").pack(anchor="w", pady=5)
entry_nome_produto = tk.Entry(frame_produto, width=30)
entry_nome_produto.pack(pady=5)

tk.Label(frame_produto, text="Categoria:", bg="white").pack(anchor="w", pady=5)
entry_categoria_produto = tk.Entry(frame_produto, width=30)
entry_categoria_produto.pack(pady=5)

tk.Label(frame_produto, text="Preço:", bg="white").pack(anchor="w", pady=5)
entry_preco_produto = tk.Entry(frame_produto, width=30)
entry_preco_produto.pack(pady=5)

btn_salvar_produto = tk.Button(frame_produto, text="Salvar", bg="#007bff", fg="white", font=("Arial", 12), command=salvar_produto)
btn_salvar_produto.pack(pady=10)

btn_voltar_produto = tk.Button(frame_produto, text="Voltar", bg="#6c757d", fg="white", font=("Arial", 12), command=voltar_menu)
btn_voltar_produto.pack()

# ------------------ Formulário de Cliente ------------------
frame_cliente = tk.Frame(janela, bg="white", padx=20, pady=20, relief="groove", bd=2)

tk.Label(frame_cliente, text="Cadastrar Cliente", font=("Arial", 16, "bold"), bg="white").pack(pady=5)

tk.Label(frame_cliente, text="Nome do Cliente:", bg="white").pack(anchor="w", pady=5)
entry_nome_cliente = tk.Entry(frame_cliente, width=30)
entry_nome_cliente.pack(pady=5)

tk.Label(frame_cliente, text="Email:", bg="white").pack(anchor="w", pady=5)
entry_email_cliente = tk.Entry(frame_cliente, width=30)
entry_email_cliente.pack(pady=5)

tk.Label(frame_cliente, text="Telefone:", bg="white").pack(anchor="w", pady=5)
entry_telefone_cliente = tk.Entry(frame_cliente, width=30)
entry_telefone_cliente.pack(pady=5)

btn_salvar_cliente = tk.Button(frame_cliente, text="Salvar", bg="#007bff", fg="white", font=("Arial", 12))
btn_salvar_cliente.pack(pady=10)

btn_voltar_cliente = tk.Button(frame_cliente, text="Voltar", bg="#6c757d", fg="white", font=("Arial", 12), command=voltar_menu)
btn_voltar_cliente.pack()

# Inicia o loop principal
janela.mainloop()
