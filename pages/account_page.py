from .base_page import BasePage
from .locators import AccountPageLocators

class AccountPage(BasePage):
    def should_be_account_page(self):
        self.should_be_account_info()
        self.should_be_sign_out_button()

    def should_be_account_info(self):
        assert self.is_element_present(AccountPageLocators.ACCOUNT_INFO), "there's no an account info"

    def should_be_sign_out_button(self):
        assert self.is_element_present(AccountPageLocators.SIGN_OUT_BUTTON), "there's no a sign out btn"
