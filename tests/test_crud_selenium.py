import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestCRUD(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Inicialize o navegador (Chrome, por exemplo)
        cls.driver = webdriver.Chrome()  # Verifique se o chromedriver está no PATH
        cls.driver.implicitly_wait(10)  # Tempo de espera implícito
        cls.base_url = "http://localhost:5000"  # URL da aplicação Flask

    def test_add_book(self):
        self.driver.get(f"{self.base_url}/add_book")
        self.driver.find_element(By.ID, "title").send_keys("Imitação de Cristo")
        self.driver.find_element(By.ID, "author").send_keys("Tomás de Kempis")
        self.driver.find_element(By.ID, "publisher").send_keys("Santa Cryz")
        self.driver.find_element(By.ID, "data_publicacao").send_keys("01/01/1418")
        self.driver.find_element(By.ID, "genero_literario").send_keys("Outro")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
        # Após redirecionamento, verifique se o livro aparece na lista
        self.assertIn("O Pequeno Príncipe", self.driver.page_source)

    def test_add_client(self):
        self.driver.get(f"{self.base_url}/add_client")
        self.driver.find_element(By.ID, "name").send_keys("Maria Silva")
        self.driver.find_element(By.ID, "cpf").send_keys("123.456.789-00")
        self.driver.find_element(By.ID, "telefone").send_keys("(11) 91234-5678")
        self.driver.find_element(By.ID, "email").send_keys("maria.silva@example.com")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
        # Após redirecionamento, verifique se o cliente aparece na lista
        self.assertIn("Maria Silva", self.driver.page_source)

    @classmethod
    def tearDownClass(cls):
        # Encerra o navegador ao fim dos testes
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
