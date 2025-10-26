import pytest
from utils import login, get_first_product, add_first_to_cart, cart_count, go_to_cart, verify_product_in_cart

def test_catalog_verification(driver):
    login(driver)
    assert driver.title == "Swag Labs"
    name, price = get_first_product(driver)
    assert name
    assert price.startswith("$")

def test_add_product_to_cart(driver):
    login(driver)
    name, _ = get_first_product(driver)
    add_first_to_cart(driver)
    assert cart_count(driver) == 1
    go_to_cart(driver)
    assert verify_product_in_cart(driver, name)