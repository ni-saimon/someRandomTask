from appium.webdriver.common.appiumby import AppiumBy
from src.pom.pages.base_page import BasePage
from src.pom.locators.category_page import Locators


class Category(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super(Category, self).__init__(driver)

    treeElectronics = (AppiumBy.XPATH, Locators.Electronics)

    def electronics(self):
        self.click(self.treeElectronics)
