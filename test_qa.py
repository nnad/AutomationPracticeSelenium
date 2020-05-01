from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage

def test_guest_can_go_to_login_page(browser):
    link = "http://automationpractice.com/index.php"
    page = MainPage(browser, link)   
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_can_login_successful(browser):
    link = "http://automationpractice.com/index.php?controller=authentication"
    page = LoginPage(browser, link)
    page.open()
    page.login_user('seleniumisgood@mail.com', '123456')
    account_page = AccountPage(browser, browser.current_url)
    account_page.should_be_account_page()
