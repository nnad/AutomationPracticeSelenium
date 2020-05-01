from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, locator):
        try:
            self.find_element(locator)
            return True
        except:
            return False

    def find_element(self, locator,time=5):
        return WebDriverWait(self.browser,time).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    def find_elements(self, locator,time=5):
        return WebDriverWait(self.browser,time).until(EC.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")

    def input(self, locator, value):
        self.find_element(locator).send_keys(value)
