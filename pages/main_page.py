from .base_page import BasePage
from .login_page import LoginPage
from .locators import MainPageLocators

class MainPage(BasePage):
    def go_to_login_page(self):
        self.find_element(MainPageLocators.LOGIN_LINK).click()

    def get_subscription(self, email):
        self.input(MainPageLocators.SUBSCRIPTION_EMAIL_FIELD,  email)
        self.find_element(MainPageLocators.SUBSCRIPTION_BUTTON).click()

    def search_item(self, query):
        self.input(MainPageLocators.SEARCH_FIELD, query)
        self.find_element(MainPageLocators.SEARCH_BUTTON).click()

    def go_to_shopping_cart(self):
        self.find_element(MainPageLocators.CART_BUTTON).click()
