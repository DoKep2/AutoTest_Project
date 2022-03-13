import math
from .main_page import MainPage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(MainPage):
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_cart_add_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BTN), "cart add button not found"

    def add_product_to_cart(self):
        add_to_cart_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
        add_to_cart_btn.click()
        self.solve_quiz_and_get_code()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def added_product_with_corresponding_name(self):
        name = self.get_product_name()
        self.add_product_to_cart()
        corresponding_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert name == corresponding_name, f"Invalid added product name: {corresponding_name} instead {name}"

    def added_product_with_corresponding_price(self):
        price = self.get_product_price()
        self.add_product_to_cart()
        corresponding_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text
        assert price == corresponding_price, f"Invalid added product price: {corresponding_price} instead {price}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
