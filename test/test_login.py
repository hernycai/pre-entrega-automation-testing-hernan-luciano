import pytest
from utils import login

def test_successful_login(driver):
    login(driver)
    assert "/inventory.html" in driver.current_url
    assert "Products" in driver.page_source
    assert "Swag Labs" in driver.title
