import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_cart_button_exists(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    answer = WebDriverWait(browser,3).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.btn-add-to-basket')), "Add to cart button doesn't exist!")
    assert answer
