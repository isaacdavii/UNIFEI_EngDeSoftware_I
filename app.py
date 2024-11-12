import webbrowser
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from threading import Timer
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Certifique-se de que o caminho está correto
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

logging.basicConfig(level=logging.DEBUG)

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

# Modelo de dados para Gênero Literário
class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

# Modelo de dados para Empréstimo
class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    loan_date = db.Column(db.String(10), nullable=False)  # Formato DD/MM/AAAA
    return_date = db.Column(db.String(10), nullable=False)  # Formato DD/MM/AAAA
    status = db.Column(db.String(10), nullable=False, default='open')

    client = db.relationship('Client', backref=db.backref('loans', lazy=True))
    book = db.relationship('Book', backref=db.backref('loans', lazy=True))

# Criação das tabelas no banco de dados (se necessário)
with app.app_context():
    try:
        db.create_all()
        app.logger.info("Database tables created successfully")
    except Exception as e:
        app.logger.error(f"Error creating database tables: {str(e)}")

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
    genres = Genre.query.all()
    return render_template('add_book.html', genres=genres)

# Rota para listar livros
@app.route('/list_books')
def list_books():
    books = Book.query.all()
    return render_template('list_books.html', books=books)

# Rota para editar um livro
@app.route('/edit_book/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = Book.query.get_or_404(book_id)
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.publisher = request.form['publisher']
        book.data_publicacao = request.form['data_publicacao']
        book.genero_literario = request.form['genero_literario']
        
        db.session.commit()
        return redirect(url_for('list_books'))
    genres = Genre.query.all()
    return render_template('edit_book.html', book=book, genres=genres)

# Rota para excluir um livro
@app.route('/delete_book/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('list_books'))

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

# Rota para editar um cliente
@app.route('/edit_client/<int:client_id>', methods=['GET', 'POST'])
def edit_client(client_id):
    client = Client.query.get_or_404(client_id)
    if request.method == 'POST':
        client.name = request.form['name']
        client.cpf = request.form['cpf']
        client.telefone = request.form['telefone']
        client.email = request.form['email']
        
        db.session.commit()
        return redirect(url_for('list_clients'))
    return render_template('edit_client.html', client=client)

# Rota para excluir um cliente
@app.route('/delete_client/<int:client_id>', methods=['POST'])
def delete_client(client_id):
    client = Client.query.get_or_404(client_id)
    db.session.delete(client)
    db.session.commit()
    return redirect(url_for('list_clients'))

# Rotas para gerenciar gêneros literários
@app.route('/manage_genres')
def manage_genres():
    genres = Genre.query.all()
    return render_template('manage_genres.html', genres=genres)

@app.route('/add_genre', methods=['POST'])
def add_genre():
    name = request.form['name']
    new_genre = Genre(name=name)
    db.session.add(new_genre)
    db.session.commit()
    return redirect(url_for('manage_genres'))

@app.route('/edit_genre/<int:genre_id>', methods=['GET', 'POST'])
def edit_genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    if request.method == 'POST':
        genre.name = request.form['name']
        db.session.commit()
        return redirect(url_for('manage_genres'))
    return render_template('edit_genre.html', genre=genre)

@app.route('/delete_genre/<int:genre_id>', methods=['POST'])
def delete_genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    db.session.delete(genre)
    db.session.commit()
    return redirect(url_for('manage_genres'))

# Rota para registrar um novo empréstimo
@app.route('/loan')
def loan():
    clients = Client.query.all()
    books = Book.query.all()
    return render_template('register_loan.html', clients=clients, books=books)

@app.route('/register_loan', methods=['POST'])
def register_loan():
    try:
        client_id = request.form['client_id']
        book_id = request.form['book_id']
        loan_date = request.form['loan_date']
        return_date = request.form['return_date']
        
        new_loan = Loan(client_id=client_id, book_id=book_id, loan_date=loan_date, return_date=return_date, status='open')
        
        db.session.add(new_loan)
        db.session.commit()
        
        return redirect(url_for('list_loans'))
    except Exception as e:
        app.logger.error(f"Error registering loan: {str(e)}")
        return str(e)

# Rota para listar empréstimos
@app.route('/list_loans')
def list_loans():
    try:
        app.logger.debug("Accessing list_loans route")
        
        loans = Loan.query.options(
            db.joinedload(Loan.client),
            db.joinedload(Loan.book)
        ).all()
        
        app.logger.debug(f"Found {len(loans)} loans")
        
        return render_template('list_loans.html', loans=loans)
    except Exception as e:
        app.logger.error(f"Error in list_loans: {str(e)}")
        return f"Error loading loans: {str(e)}", 500

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