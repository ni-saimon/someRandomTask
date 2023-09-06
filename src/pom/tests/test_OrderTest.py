import allure

from src.pom.utility.coftest import GetDriver
from src.pom.pages.disclaimer_page import Disclaimer


class TestOrder(GetDriver):

    @allure.step("Complete an Order")
    def test_order(self):
        app = Disclaimer(self.driver)
        app.acceptDisclaimer()
