from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CLASS_NAME, "login")
    SUBSCRIPTION_EMAIL_FIELD = (By.ID, "newsletter-input")
    SUBSCRIPTION_BUTTON = (By.NAME, "submitNewsletter")
    SEARCH_FIELD = (By.ID, "search_query_top")
    SEARCH_BUTTON = (By.NAME, "submit_search")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#create-account_form")
    EMAIL_FIELD = (By.CSS_SELECTOR,"#email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#passwd")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#SubmitLogin")

class AccountPageLocators:
    ACCOUNT_INFO = (By.CLASS_NAME, 'info-account')
    SIGN_OUT_BUTTON = (By.CLASS_NAME, 'logout')
