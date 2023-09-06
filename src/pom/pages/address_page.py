from appium.webdriver.common.appiumby import AppiumBy
from src.pom.pages.base_page import BasePage
from src.pom.locators.checkout_page import Address
from Data.guestcutomerinfo import GuestInformation


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

    def information(self):
        self.send_keys(self.FirstName, GuestInformation.firstName)
        self.send_keys(self.LastName, GuestInformation.lastName)
        self.send_keys(self.Email, GuestInformation.email)
        self.click(self.CountryDropDown)
        self.click(self.CountryName)
        self.click(self.StateDropDown)
        self.click(self.StateName)
        self.send_keys(self.Company, GuestInformation.company)
        self.swipeDown()
        self.send_keys(self.City, GuestInformation.city)
        self.send_keys(self.Street1, GuestInformation.street1)
        self.send_keys(self.ZipCode, GuestInformation.zip)
        self.send_keys(self.Phone, GuestInformation.phone)
        self.send_keys(self.Fax, GuestInformation.fax)
        self.click(self.continueBtn)

