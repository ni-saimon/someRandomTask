import allure
import unittest
from appium import webdriver


class GetDriver(unittest.TestCase):

    @allure.step("nopstationCart")
    def setUp(self):
        capabilities = dict(
            platformName='Android',
            automationName='uiautomator2',
            deviceName='emulator-5554',
            app='C:\\Users\\nafiz\\Downloads\\nopstationCart_4.40.apk',
            language='en',
            locale='US'
        )
        url = 'http://localhost:4723/wd/hub'
        self.driver = webdriver.Remote(url, capabilities)

    def tearDown(self):
        print("Test Completed")


if __name__ == "__main__":
    unittest.main()
