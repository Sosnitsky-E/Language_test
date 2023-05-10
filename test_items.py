import time

from selenium.webdriver.common.by import By


def test_add_to_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    actual_result = add_to_basket_button.is_displayed()
    assert actual_result == True, "The button does not display on the web page"
