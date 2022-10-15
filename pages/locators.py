from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "form.add-to-basket > button")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main>.price_color")
    ALERT_SUCCESS = (By.CSS_SELECTOR, "#messages > .alert-success")
    ALERT_INFO = (By.CSS_SELECTOR, ".alert-info")
    ALERT_SUCCESS_NAME = (By.CSS_SELECTOR, "#messages div div strong ")
    ALERT_INFO_PRICE = (By.CSS_SELECTOR, "#messages div p strong")
