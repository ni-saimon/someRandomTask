from appium.webdriver.common.appiumby import AppiumBy
from src.pom.pages.base_page import BasePage
from src.pom.locators.home_page import OurCategories
from src.pom.locators.navigation_drawer_page import Locators


class HomePage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super(HomePage, self).__init__(driver)

    Electronics = (AppiumBy.XPATH, OurCategories.Electronics)
    searchButton = (AppiumBy.ID, Locators.search)
    srcTxt = (AppiumBy.ID, Locators.src_text)

    def ourCategories(self):
        self.swipeLeft()
        self.swipeLeft()
        self.click(self.Electronics)

    def search(self):
        self.click(self.searchButton)

    def searchItem(self, key):
        self.send_keys(self.srcTxt, key)
        self.driver.press_keycode(66)
