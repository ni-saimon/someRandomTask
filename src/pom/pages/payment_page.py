from appium.webdriver.common.appiumby import AppiumBy
from src.pom.pages.base_page import BasePage
from src.pom.locators.checkout_page import Address
from src.pom.locators.checkout_page import Payment


class PaymentType(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super(PaymentType, self).__init__(driver)

    nagadPayment = (AppiumBy.XPATH, Payment.Nagad)
    checkMoney = (AppiumBy.XPATH, Payment.CheckMoney)
    continueBtn = (AppiumBy.ID, Address.btnContinue)
    nextBtn = (AppiumBy.XPATH, Payment.confirmButton)

    def checkMoneyOrderPayment(self):
        self.click(self.nagadPayment)
        self.swipeDownLong()
        self.click(self.checkMoney)
        self.click(self.continueBtn)
        self.click(self.nextBtn)
