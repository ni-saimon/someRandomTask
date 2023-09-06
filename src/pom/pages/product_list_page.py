from appium.webdriver.common.appiumby import AppiumBy
from src.pom.pages.base_page import BasePage
from src.pom.locators.product_list_page import Locators


class ProductList(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super(ProductList, self).__init__(driver)

    firstItems = (AppiumBy.ID, Locators.firstItemView)

    def firstItem(self):
        self.click(self.firstItems)
