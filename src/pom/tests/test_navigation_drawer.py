import allure
import unittest
from src.pom.utility.coftest import GetDriver
from src.pom.pages.disclaimer_page import Disclaimer
from src.pom.pages.navigation_drawer_page import NavigationDrawer


class TestNavigationDrawer(unittest.TestCase):

    driver = GetDriver().setUp()

    @allure.step("Navigate to Category")
    def test_navigation_drawer(self):
        disc = Disclaimer(self.driver)
        disc.acceptDisclaimer()
        nav = NavigationDrawer(self.driver)
        nav.category()

