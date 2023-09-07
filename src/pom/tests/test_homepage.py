import allure
from src.pom.utility.coftest import GetDriver
from src.pom.pages.disclaimer_page import Disclaimer
from src.pom.pages.homepage_page import HomePage


class TestHomePage:

    driver = GetDriver().setUp()

    @allure.step("Navigate to Our Categories")
    def test_homepage(self):
        disc = Disclaimer(self.driver)
        disc.acceptDisclaimer()
        nav = HomePage(self.driver)
        nav.ourCategories()
