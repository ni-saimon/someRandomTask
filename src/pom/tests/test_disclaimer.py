import allure

from src.pom.utility.coftest import GetDriver
from src.pom.pages.disclaimer_page import Disclaimer


class TestDisclaimer:

    driver = GetDriver().setUp()

    @allure.testcase("Accept Disclaimer")
    def test_disclaimer(self):
        disc = Disclaimer(self.driver)
        disc.acceptDisclaimer()
