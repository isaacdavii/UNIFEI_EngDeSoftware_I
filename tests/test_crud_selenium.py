import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCRUD(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Inicialize o navegador (Chrome, por exemplo)
        cls.driver = webdriver.Chrome()  # Verifique se o chromedriver está no PATH
        cls.driver.implicitly_wait(10)  # Tempo de espera implícito
        cls.base_url = "http://127.0.0.1:5000/"  # URL da aplicação Flask

    def add_client(self, name, cpf, telefone, email):
        self.driver.get(f"{self.base_url}/add_client")
        self.driver.find_element(By.ID, "name").send_keys(name)
        self.driver.find_element(By.ID, "cpf").send_keys(cpf)
        self.driver.find_element(By.ID, "telefone").send_keys(telefone)
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
        # Após redirecionamento, verifique se o cliente aparece na lista
        self.assertIn(name, self.driver.page_source)

    def add_book(self, title, author, publisher, data_publicacao, genero_literario):
        self.driver.get(f"{self.base_url}/add_book")
        self.driver.find_element(By.ID, "title").send_keys(title)
        self.driver.find_element(By.ID, "author").send_keys(author)
        self.driver.find_element(By.ID, "publisher").send_keys(publisher)
        self.driver.find_element(By.ID, "data_publicacao").send_keys(data_publicacao)
        self.driver.find_element(By.ID, "genero_literario").send_keys(genero_literario)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
        # Após redirecionamento, verifique se o livro aparece na lista
        self.assertIn(title, self.driver.page_source)

    def test_add_clients(self):
        clients = [
            {"name": "Carolina", "cpf": "123.456.789-01", "telefone": "(11) 91234-5678", "email": "carolina@example.com"},
            {"name": "Marcos", "cpf": "234.567.890-12", "telefone": "(21) 99376-4852", "email": "marcos@example.com"},
            {"name": "Tiago", "cpf": "345.678.901-23", "telefone": "(31) 98765-5689", "email": "tiago@example.com"},
            {"name": "Bartolomeu", "cpf": "456.789.012-34", "telefone": "(41) 98673-3210", "email": "bartolomeu@example.com"},
            {"name": "Pedro ", "cpf": "567.890.123-45", "telefone": "(51) 96543-7264", "email": "pedro@example.com"}
        ]
        
        for client in clients:
            self.add_client(client["name"], client["cpf"], client["telefone"], client["email"])

    def test_add_books(self):
        books = [
            {"title": "Orgulho e Preconceito", "author": "Jane Austen", "publisher": "Penguin", "data_publicacao": "1813", "genero_literario": "Romance"},
            {"title": "Jane Eyre", "author": "Charlotte Brontë", "publisher": "Smith, Elder & Co.", "data_publicacao": "1847", "genero_literario": "Romance"},
            {"title": "O Morro dos Ventos Uivantes", "author": "Emily Brontë", "publisher": "Thomas Cautley Newby", "data_publicacao": "1847", "genero_literario": "Romance"},
            {"title": "Drácula", "author": "Bram Stoker", "publisher": "Archibald Constable and Company", "data_publicacao": "1897", "genero_literario": "Terror"},
            {"title": "Frankenstein", "author": "Mary Shelley", "publisher": "Lackington, Hughes, Harding, Mavor & Jones", "data_publicacao": "1818", "genero_literario": "Terror"},
            {"title": "O Iluminado", "author": "Stephen King", "publisher": "Doubleday", "data_publicacao": "1977", "genero_literario": "Terror"},
            {"title": "1984", "author": "George Orwell", "publisher": "Secker & Warburg", "data_publicacao": "1949", "genero_literario": "Ficção"},
            {"title": "Admirável Mundo Novo", "author": "Aldous Huxley", "publisher": "Chatto & Windus", "data_publicacao": "1932", "genero_literario": "Ficção"},
            {"title": "Neuromancer", "author": "William Gibson", "publisher": "Ace", "data_publicacao": "1984", "genero_literario": "Ficção"},
            {"title": "O Senhor dos Anéis", "author": "J.R.R. Tolkien", "publisher": "Allen & Unwin", "data_publicacao": "1954", "genero_literario": "Fantasia"},
            {"title": "Harry Potter e a Pedra Filosofal", "author": "J.K. Rowling", "publisher": "Bloomsbury", "data_publicacao": "1997", "genero_literario": "Fantasia"},
            {"title": "O Hobbit", "author": "J.R.R. Tolkien", "publisher": "George Allen & Unwin", "data_publicacao": "1937", "genero_literario": "Fantasia"},
            {"title": "Como Fazer Amigos e Influenciar Pessoas", "author": "Dale Carnegie", "publisher": "Simon and Schuster", "data_publicacao": "1936", "genero_literario": "Autoajuda"},
            {"title": "O Poder do Hábito", "author": "Charles Duhigg", "publisher": "Random House", "data_publicacao": "2012", "genero_literario": "Psicologia"},
            {"title": "Os 7 Hábitos das Pessoas Altamente Eficazes", "author": "Stephen R. Covey", "publisher": "Free Press", "data_publicacao": "1989", "genero_literario": "Autoajuda"},
            {"title": "A República", "author": "Platão", "publisher": "Penguin", "data_publicacao": "380 a.C.", "genero_literario": "Filosofia"},
            {"title": "Assim Falou Zaratustra", "author": "Friedrich Nietzsche", "publisher": "Penguin", "data_publicacao": "1883", "genero_literario": "Filosofia"},
            {"title": "Crítica da Razão Pura", "author": "Immanuel Kant", "publisher": "N/A", "data_publicacao": "1781", "genero_literario": "Filosofia"},
            {"title": "O Pequeno Príncipe", "author": "Antoine de Saint-Exupéry", "publisher": "Reynal & Hitchcock", "data_publicacao": "1943", "genero_literario": "Fábula"},
            {"title": "As Aventuras de Pinóquio", "author": "Carlo Collodi", "publisher": "Felice Paggi", "data_publicacao": "1883", "genero_literario": "Fábula"},
            {"title": "A Tartaruga e a Lebre", "author": "Esopo", "publisher": "N/A", "data_publicacao": "N/A", "genero_literario": "Fábula"},
            {"title": "Hamlet", "author": "William Shakespeare", "publisher": "N/A", "data_publicacao": "1603", "genero_literario": "Drama"},
            {"title": "Romeu e Julieta", "author": "William Shakespeare", "publisher": "N/A", "data_publicacao": "1597", "genero_literario": "Drama"},
            {"title": "A Casa de Bernarda Alba", "author": "Federico García Lorca", "publisher": "N/A", "data_publicacao": "1936", "genero_literario": "Drama"},
            {"title": "Sapiens: Uma Breve História da Humanidade", "author": "Yuval Noah Harari", "publisher": "Harper", "data_publicacao": "2011", "genero_literario": "História"},
            {"title": "Guns, Germs, and Steel", "author": "Jared Diamond", "publisher": "W.W. Norton & Company", "data_publicacao": "1997", "genero_literario": "História"},
            {"title": "A People's History of the United States", "author": "Howard Zinn", "publisher": "Harper & Row", "data_publicacao": "1980", "genero_literario": "História"},
            {"title": "Dom Quixote", "author": "Miguel de Cervantes", "publisher": "Francisco de Robles", "data_publicacao": "1605", "genero_literario": "Clássico"},
            {"title": "Moby Dick", "author": "Herman Melville", "publisher": "Harper & Brothers", "data_publicacao": "1851", "genero_literario": "Clássico"},
            {"title": "Os Miseráveis", "author": "Victor Hugo", "publisher": "A. Lacroix, Verboeckhoven & Cie", "data_publicacao": "1862", "genero_literario": "Clássico"},
            {"title": "O Menino Maluquinho", "author": "Ziraldo", "publisher": "Melhoramentos", "data_publicacao": "1980", "genero_literario": "Literatura Infantil"},
            {"title": "Alice no País das Maravilhas", "author": "Lewis Carroll", "publisher": "Macmillan", "data_publicacao": "1865", "genero_literario": "Literatura Infantil"},
            {"title": "O Mágico de Oz", "author": "L. Frank Baum", "publisher": "George M. Hill Company", "data_publicacao": "1900", "genero_literario": "Literatura Infantil"},
            {"title": "A Bíblia Sagrada", "author": "Diversos", "publisher": "N/A", "data_publicacao": "N/A", "genero_literario": "Religião"},
            {"title": "O Alcorão", "author": "Diversos", "publisher": "N/A", "data_publicacao": "N/A", "genero_literario": "Religião"},
            {"title": "O Livro dos Espíritos", "author": "Allan Kardec", "publisher": "N/A", "data_publicacao": "1857", "genero_literario": "Religião"}
        ]
        
        for book in books:
            self.add_book(book["title"], book["author"], book["publisher"], book["data_publicacao"], book["genero_literario"])

    @classmethod
    def tearDownClass(cls):
        # Encerra o navegador ao fim dos testes
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()