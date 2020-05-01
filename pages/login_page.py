from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):
        assert self.is_element_present(LoginPageLocators.LOGIN_FORM), "there's no a login form"

    def should_be_register_form(self):
        assert self.is_element_present(LoginPageLocators.REGISTRATION_FORM), "there's no a reg form"

    def login_user(self, email, password):
        self.should_be_login_page()
        self.input(LoginPageLocators.EMAIL_FIELD, email)
        self.input(LoginPageLocators.PASSWORD_FIELD, password)
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click() 
