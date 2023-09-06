from appium.webdriver.common.appiumby import AppiumBy
from src.pom.pages.base_page import BasePage
from src.pom.locators.product_list_page import Locators


class ProductList(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super(ProductList, self).__init__(driver)

    firstItem = (AppiumBy.ID, Locators.firstItemView)

    def FirstItem(self):
        self.click(self.firstItem)
