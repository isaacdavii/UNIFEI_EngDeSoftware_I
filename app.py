from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definindo o modelo de dados para o Livro
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)

# Definindo o modelo de dados para o Cliente
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)

# Criação das tabelas no banco de dados
with app.app_context():
    db.create_all()

# Rota para adicionar um novo livro
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        publisher = request.form['publisher']
        new_book = Book(title=title, author=author, publisher=publisher)
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
        new_client = Client(name=name, cpf=cpf)
        db.session.add(new_client)
        db.session.commit()
        return redirect(url_for('list_clients'))
    return render_template('add_client.html')

# Rota para listar clientes
@app.route('/list_clients')
def list_clients():
    clients = Client.query.all()
    return render_template('list_clients.html', clients=clients)

if __name__ == '__main__':
    app.run(debug=True)
