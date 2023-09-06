from appium.webdriver.common.appiumby import AppiumBy
from src.pom.pages.base_page import BasePage
from src.pom.locators.disclaimer_page import Locators


class Disclaimer(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super(Disclaimer, self).__init__(driver)

    acceptButton = (AppiumBy.ID, Locators.accept)

    def acceptDisclaimer(self):
        self.click(self.acceptButton)
