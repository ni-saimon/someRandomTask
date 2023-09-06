import allure
import unittest
from src.pom.utility.coftest import GetDriver
from src.pom.pages.disclaimer_page import Disclaimer
from src.pom.pages.navigation_drawer_page import NavigationDrawer
from src.pom.pages.category_page import Category


class TestCatElectronics(unittest.TestCase):

    driver = GetDriver().setUp()

    @allure.step("Search Mattress Bedroom from Electronics Category")
    def test_navigation_drawer(self):
        disc = Disclaimer(self.driver)
        disc.acceptDisclaimer()
        nav = NavigationDrawer(self.driver)
        nav.category()
        elec = Category(self.driver)
        elec.electronics()
        nav.search()
        nav.searchItem("Mattress Bedroom")
