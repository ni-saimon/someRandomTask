from appium.webdriver.common.appiumby import AppiumBy
from src.pom.pages.base_page import BasePage
from src.pom.locators.checkout_page import Address
from Data.data import Information


class FillUpAddress(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super(FillUpAddress, self).__init__(driver)

    FirstName = (AppiumBy.ID, Address.FirstName)
    LastName = (AppiumBy.ID, Address.LastName)
    Email = (AppiumBy.ID, Address.Email)
    CountryDropDown = (AppiumBy.ID, Address.country)
    CountryName = (AppiumBy.XPATH, Address.countryName)
    StateDropDown = (AppiumBy.ID, Address.state)
    StateName = (AppiumBy.XPATH, Address.stateName)
    Company = (AppiumBy.ID, Address.company)
    City = (AppiumBy.ID, Address.city)
    Street1 = (AppiumBy.ID, Address.street1)
    ZipCode = (AppiumBy.ID, Address.zipCode)
    Phone = (AppiumBy.ID, Address.phone)
    Fax = (AppiumBy.ID, Address.fax)
    continueBtn = (AppiumBy.ID, Address.btnContinue)

    def customerInformation(self):
        self.send_keys(self.FirstName, Information.firstName)
        self.send_keys(self.LastName, Information.lastName)
        self.send_keys(self.Email, Information.email)
        self.click(self.CountryDropDown)
        self.click(self.CountryName)
        self.click(self.StateDropDown)
        self.click(self.StateName)
        self.send_keys(self.Company, Information.company)
        self.swipeDown()
        self.send_keys(self.City, Information.city)
        self.send_keys(self.Street1, Information.street1)
        self.send_keys(self.ZipCode, Information.zip)
        self.send_keys(self.Phone, Information.phone)
        self.send_keys(self.Fax, Information.fax)
        self.click(self.continueBtn)
