from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

# Caminhos dos arquivos CSV
ARQUIVO_PRODUTO = "produtos.csv"
ARQUIVO_CLIENTE = "clientes.csv"

# Função para criar arquivos CSV caso não existam
def criar_arquivos_csv():
    if not os.path.exists(ARQUIVO_PRODUTO):
        with open(ARQUIVO_PRODUTO, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Nome", "Categoria", "Preço"])
    
    if not os.path.exists(ARQUIVO_CLIENTE):
        with open(ARQUIVO_CLIENTE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Nome", "Email", "Telefone"])

# Rota principal - Renderiza o formulário HTML
@app.route("/")
def index():
    return render_template("index.html")

# Rota para salvar os dados do produto
@app.route("/cadastrar_produto", methods=["POST"])
def cadastrar_produto():
    nome = request.form["nomeProduto"]
    categoria = request.form["categoriaProduto"]
    preco = request.form["precoProduto"]

    if nome and categoria and preco:
        with open(ARQUIVO_PRODUTO, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([nome, categoria, preco])
        return redirect(url_for("index"))
    else:
        return "Preencha todos os campos do Produto!", 400

# Rota para salvar os dados do cliente
@app.route("/cadastrar_cliente", methods=["POST"])
def cadastrar_cliente():
    nome = request.form["nomeCliente"]
    email = request.form["emailCliente"]
    telefone = request.form["telefoneCliente"]

    if nome and email and telefone:
        with open(ARQUIVO_CLIENTE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([nome, email, telefone])
        return redirect(url_for("index"))
    else:
        return "Preencha todos os campos do Cliente!", 400

if __name__ == "__main__":
    criar_arquivos_csv()
    app.run(debug=True)
