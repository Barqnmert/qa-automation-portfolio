from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com/"

def run_all_tests():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        test_login_success(driver, wait)
        test_login_negative(driver, wait)
        print("ALL TESTS PASSED ✅")
    finally:
        driver.quit()

def reset_to_login(driver, wait):
    driver.get(BASE_URL)
    # Login sayfasındaki username alanı görünene kadar bekle
    wait.until(EC.visibility_of_element_located((By.ID, "user-name")))

def login(driver, username, password):
    # Alanları temizle (tekrar tekrar koşarken önemli)
    user = driver.find_element(By.ID, "user-name")
    pwd = driver.find_element(By.ID, "password")

    user.clear()
    pwd.clear()

    user.send_keys(username)
    pwd.send_keys(password)
    driver.find_element(By.ID, "login-button").click()

def test_login_success(driver, wait):
    reset_to_login(driver, wait)

    login(driver, "standard_user", "secret_sauce")

    # Inventory sayfasına gelene kadar bekle
    wait.until(EC.url_contains("inventory"))
    assert "inventory" in driver.current_url
    print("test_login_success PASSED")

def test_login_negative(driver, wait):
    reset_to_login(driver, wait)

    login(driver, "standard_user", "WRONG_PASSWORD")

    # Hata mesajı görünene kadar bekle
    error_el = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )
    assert "Username and password do not match" in error_el.text
    print("test_login_negative PASSED")

if __name__ == "__main__":
    run_all_tests()
