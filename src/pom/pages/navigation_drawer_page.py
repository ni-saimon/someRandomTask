from appium.webdriver.common.appiumby import AppiumBy
from src.pom.pages.base_page import BasePage
from src.pom.locators.navigation_drawer_page import Locators


class NavigationDrawer(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super(NavigationDrawer, self).__init__(driver)

    categoryButton = (AppiumBy.ID, Locators.category)
    searchButton = (AppiumBy.ID, Locators.search)
    srcTxt = (AppiumBy.ID, Locators.src_text)

    def category(self):
        self.click(self.categoryButton)

    def search(self):
        self.click(self.searchButton)

    def searchItem(self, key):
        self.send_keys(self.srcTxt, key)
        self.driver.press_keycode(66)
