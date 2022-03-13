from pages.base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_not_be_cart_items(self):
        assert self.is_not_element_present(*CartPageLocators.BASKET_ITEMS_DIV), \
            "Cart items are presented, but should not be"

    def should_disappear_cart_items(self):
        assert self.is_disappeared(*CartPageLocators.BASKET_ITEMS_DIV), \
            "Cart items aren't disappeared, but should be"

    def should_be_empty_cart_title(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_CART_TITLE), \
            "Empty cart title is not presented, but should be"
