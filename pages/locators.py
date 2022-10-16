from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "header span > a.btn")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "form.add-to-basket > button")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main>.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-success")
    ALERT_INFO = (By.CSS_SELECTOR, ".alert-info")
    SUCCESS_MESSAGE_NAME = (By.CSS_SELECTOR, "#messages div div strong ")
    ALERT_INFO_PRICE = (By.CSS_SELECTOR, "#messages div p strong")


class BasketPageLocators():
    # EMPTY_BASKET_MESSAGE = (By.XPATH, "//p[contains(text(), 'Your basket is empty')]") # Для английского
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")  # Для всех языков
    ITEM = (By.CSS_SELECTOR, ".basket-items")
