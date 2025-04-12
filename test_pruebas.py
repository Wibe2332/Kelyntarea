import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import os


class SauceDemoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report_file = os.path.join(os.path.expanduser("~"), "Desktop", "ReportePruebas.html")
        print(f"Report will be saved to: {cls.report_file}")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)
        self.base_url = "https://www.saucedemo.com/"
        self.valid_username = "standard_user"
        self.valid_password = "secret_sauce"

        self.driver.get(self.base_url)
        self.perform_login()

    def tearDown(self):
        self.driver.quit()

    def perform_login(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(self.valid_username)
        self.driver.find_element(By.ID, "password").send_keys(self.valid_password)
        self.driver.find_element(By.ID, "login-button").click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".inventory_list")))

    def test_login_exitoso(self):
        title = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".title"))).text
        self.assertEqual("Products", title.strip(), "El título después de iniciar sesión no coincide.")

    def test_agregar_producto_al_carrito(self):
        add_to_cart = self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
        add_to_cart.click()
        cart_badge = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge"))).text
        self.assertEqual("1", cart_badge, "El número en el carrito no es el esperado.")

    def test_ver_detalles_producto(self):
        producto_esperado = "Sauce Labs Backpack"
        producto = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'inventory_item_name') and text()='Sauce Labs Backpack']")))
        producto.click()

        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".inventory_details_container")))
        nombre_detalle = self.driver.find_element(By.CSS_SELECTOR, ".inventory_details_name").text.strip()
        precio_detalle = self.driver.find_element(By.CSS_SELECTOR, ".inventory_details_price").text.strip()

        self.assertEqual(producto_esperado, nombre_detalle, "El nombre del producto en detalles no coincide.")
        self.assertTrue(precio_detalle.startswith("$"), "El precio no tiene el símbolo '$'.")

    def test_filtrar_por_precio_bajo_alto(self):
        dropdown = Select(self.driver.find_element(By.CSS_SELECTOR, ".product_sort_container"))
        dropdown.select_by_value("lohi")

        precios_elementos = self.driver.find_elements(By.CSS_SELECTOR, ".inventory_item_price")
        precios = [float(p.text.replace("$", "")) for p in precios_elementos]
        precios_ordenados = sorted(precios)

        self.assertEqual(precios, precios_ordenados, "Los productos no están ordenados de menor a mayor precio.")

    def test_continuar_con_checkout(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".shopping_cart_link"))).click()

        self.wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, ".cart_item")) > 0)
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        self.wait.until(EC.url_contains("checkout-step-one.html"))

        info_title = self.wait.until(EC.presence_of_element_located((
            By.XPATH, "//span[@class='title' and text()='Checkout: Your Information']"))).text

        self.assertEqual("CHECKOUT: YOUR INFORMATION", info_title.strip().upper())
         
#Kelyn mmg




