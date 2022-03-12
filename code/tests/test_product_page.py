import pytest
from pages.product_page import ProductPage

link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"


#@pytest.mark.skip
def test_guest_should_see_cart_add_btn(browser):
    #link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_cart_add_btn()


#@pytest.mark.skip
def test_can_add_product_to_cart(browser):
    #link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()


def test_add_product_with_corresponding_name(browser):
    #link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.added_product_with_corresponding_name()


def test_add_product_with_corresponding_price(browser):
    #link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.added_product_with_corresponding_price()