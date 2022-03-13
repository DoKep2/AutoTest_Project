from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_BTN = (By.XPATH, "//span/a[@class = 'btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class CartPageLocators():
    BASKET_ITEMS_DIV = (By.CSS_SELECTOR, "basket-items")
    EMPTY_CART_TITLE = (By.XPATH, '//p/a[@href]')

# class MainPageLocators():


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD_REPEAT = (By.ID, "id_registration-password2")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "[name = registration_submit]")


class ProductPageLocators():
    ADD_TO_CART_BTN = (By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    ADDED_PRODUCT_NAME = (By.XPATH, "//div[@class='alertinner ']/strong")
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert.alert-safe.alert-noicon.alert-success")
