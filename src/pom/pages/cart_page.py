from appium.webdriver.common.appiumby import AppiumBy
from src.pom.pages.base_page import BasePage
from src.pom.locators.cart_page import Locators


class Checkout(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super(Checkout, self).__init__(driver)

    checkoutBtn = (AppiumBy.ID, Locators.btnCheckOut)
    guestBtn = (AppiumBy.ID, Locators.btnGuestCheckout)

    def checkout(self):
        self.click(self.checkoutBtn)

    def guestCheckout(self):
        self.click(self.guestBtn)
