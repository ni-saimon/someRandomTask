import allure
from src.pom.utility.coftest import GetDriver
from src.pom.pages.disclaimer_page import Disclaimer
from src.pom.pages.homepage_page import HomePage


class TestSearch:

    driver = GetDriver().setUp()

    @allure.step("Search Mattress Bedroom")
    def test_search(self):
        disc = Disclaimer(self.driver)
        disc.acceptDisclaimer()
        nav = HomePage(self.driver)
        nav.ourCategories()
        nav.search()
        nav.searchItem("Mattress Bedroom")
