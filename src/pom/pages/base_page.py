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

    def swipeLeft(self):
        self.driver.swipe(550, 950, 50, 950, 400)

    def swipeDown(self):
        self.driver.swipe(0, 800, 0, 0, 1000)

    def swipeDownShort(self):
        self.driver.swipe(0, 500, 0, 0, 500)

    def swipeDownLong(self):
        self.driver.swipe(500, 2000, 500, 1600, 75)
