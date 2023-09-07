import allure
import unittest
from src.pom.utility.coftest import GetDriver
from src.pom.pages.disclaimer_page import Disclaimer
from src.pom.pages.homepage_page import HomePage


class TestSearch(unittest.TestCase):

    driver = GetDriver().setUp()

    @allure.step("Search Mattress Bedroom from Electronics Category")
    def test_search(self):
        disc = Disclaimer(self.driver)
        disc.acceptDisclaimer()
        nav = HomePage(self.driver)
        nav.ourCategories()
        nav.search()
        nav.searchItem("Mattress Bedroom")
