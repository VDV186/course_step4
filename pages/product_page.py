from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_alert(self):
        self.should_be_alert_success()
        self.should_be_alert_info()
        self.alert_success_name_equal_product_name()
        self.alert_info_price_equal_product_price()

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_alert_success(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented"

    def should_be_alert_info(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_INFO), "Alert-info is not presented"

    def alert_info_price_equal_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        alert_info_price = self.browser.find_element(*ProductPageLocators.ALERT_INFO_PRICE)
        alert = alert_info_price.text
        product = product_price.text
        assert alert == product, "Alert info price is non equal product price"

    def alert_success_name_equal_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        success_message_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_NAME)
        alert = success_message_name.text
        product = product_name.text
        assert alert == product, "Success message name is non equal product name"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success should be disappeared, but not"
