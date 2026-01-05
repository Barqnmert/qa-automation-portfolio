import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com/"

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    yield d
    d.quit()

def login(driver, username, password):
    user = driver.find_element(By.ID, "user-name")
    pwd = driver.find_element(By.ID, "password")

    user.clear()
    pwd.clear()

    user.send_keys(username)
    pwd.send_keys(password)

    driver.find_element(By.ID, "login-button").click()

def test_login_success(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)

    login(driver, "standard_user", "secret_sauce")

    wait.until(EC.url_contains("inventory"))
    assert "inventory" in driver.current_url

def test_login_negative(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)

    login(driver, "standard_user", "WRONG_PASSWORD")

    error_el = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )
    assert "Username and password do not match" in error_el.text
