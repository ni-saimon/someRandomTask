from appium.webdriver.common.appiumby import AppiumBy
from src.pom.pages.base_page import BasePage
from src.pom.locators.checkout_page import Address
from src.pom.locators.checkout_page import Shipping


class ShipmentType(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super(ShipmentType, self).__init__(driver)

    NextDayAir = (AppiumBy.XPATH, Shipping.NextDayAir)
    continueBtn = (AppiumBy.ID, Address.btnContinue)

    def shippingNextDayAir(self):
        self.click(self.NextDayAir)
        self.swipeDownShort()
        self.click(self.continueBtn)
