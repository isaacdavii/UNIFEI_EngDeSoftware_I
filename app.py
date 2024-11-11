from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import webbrowser
from threading import Timer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Atualizando o modelo de dados para o Livro
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=True)
    data_publicacao = db.Column(db.String(10), nullable=True)  # Formato DD/MM/AAAA
    genero_literario = db.Column(db.String(50), nullable=True)

# Atualizando o modelo de dados para o Cliente
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)
    telefone = db.Column(db.String(15), nullable=True)  # Formato (XX) XXXXX-XXXX
    email = db.Column(db.String(100), nullable=True)

# Criação das tabelas no banco de dados
with app.app_context():
    db.create_all()

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('principal.html')

# Rota para adicionar um novo livro
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        publisher = request.form['publisher']
        data_publicacao = request.form['data_publicacao']
        genero_literario = request.form['genero_literario']
        
        new_book = Book(title=title, author=author, publisher=publisher, 
                        data_publicacao=data_publicacao, genero_literario=genero_literario)
        
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('list_books'))
    return render_template('add_book.html')

# Rota para listar livros
@app.route('/list_books')
def list_books():
    books = Book.query.all()
    return render_template('list_books.html', books=books)

# Rota para adicionar um novo cliente
@app.route('/add_client', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        name = request.form['name']
        cpf = request.form['cpf']
        telefone = request.form.get('telefone')
        email = request.form.get('email')
        
        new_client = Client(name=name, cpf=cpf, telefone=telefone, email=email)
        
        db.session.add(new_client)
        db.session.commit()
        return redirect(url_for('list_clients'))
    return render_template('add_client.html')

# Rota para listar clientes
@app.route('/list_clients')
def list_clients():
    clients = Client.query.all()
    return render_template('list_clients.html', clients=clients)

# Função para abrir as URLs automaticamente (com flag para abrir apenas uma vez)
def open_browser():
    # Use uma variável global para garantir que o navegador abre apenas uma vez
    global browser_opened
    if not browser_opened:
        webbrowser.open_new('http://127.0.0.1:5000/')
        browser_opened = True

if __name__ == '__main__':
    # Configura a flag antes de iniciar o servidor
    browser_opened = False
    # Use Timer para abrir o navegador um pouco depois do app iniciar
    Timer(1, open_browser).start()
    app.run(debug=False)  # Execute sem debug para evitar reinicializações duplicadas
