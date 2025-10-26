from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

def login(driver, username="standard_user", password="secret_sauce"):
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    wait.until(EC.url_contains("/inventory.html"))

def get_first_product(driver):
    wait = WebDriverWait(driver, 10)
    item = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
    name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
    price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
    return name, price

def add_first_to_cart(driver):
    driver.find_element(By.CSS_SELECTOR, ".btn_inventory").click()

def cart_count(driver):
    try:
        badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        return int(badge.text) if badge.is_displayed() else 0
    except:
        return 0

def go_to_cart(driver):
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

def verify_product_in_cart(driver, expected_name):
    name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    return name == expected_name