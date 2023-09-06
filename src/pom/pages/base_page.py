from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, by_locator):
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    def send_keys(self, by_locator, value):
        self.wait.until(EC.presence_of_element_located(by_locator)).send_keys(value)

    def get_text(self, by_locator):
        return self.wait.until(EC.presence_of_element_located(by_locator)).text

    def wait_for_clickable(self, by_locator):
        self.wait.until(EC.element_to_be_clickable(by_locator))

    def swipe(self):
        self.driver.swipe(0, 800, 0, 0, 1000)
