import allure
from appium import webdriver


class GetDriver(object):

    driver = None

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
        return self.driver
