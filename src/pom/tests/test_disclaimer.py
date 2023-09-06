import allure
import unittest

from src.pom.utility.coftest import GetDriver
from src.pom.pages.disclaimer_page import Disclaimer


class TestDisclaimer(unittest.TestCase):

    driver = GetDriver().setUp()

    @allure.step("Accept Disclaimer")
    def test_disclaimer(self):
        disc = Disclaimer(self.driver)
        disc.acceptDisclaimer()
