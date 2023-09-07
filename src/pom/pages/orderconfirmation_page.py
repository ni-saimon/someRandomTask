from appium.webdriver.common.appiumby import AppiumBy
from src.pom.pages.base_page import BasePage
from src.pom.locators.checkout_page import Address
from src.pom.locators.checkout_page import OrderConfirm


class OrderFinalize(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super(OrderFinalize, self).__init__(driver)

    continueBtn = (AppiumBy.ID, Address.btnContinue)
    message = (AppiumBy.ID, OrderConfirm.Message)

    def orderSuccessful(self):
        self.click(self.continueBtn)
        return self.get_text(self.message)
