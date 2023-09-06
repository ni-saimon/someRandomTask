from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pom.pages.base_page import BasePage

acceptButton = (AppiumBy.ID, "btnAccept")


class Disclaimer(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super(Disclaimer, self).__init__(driver)

    def acceptDisclaimer(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, "btnAccept"))).click()
