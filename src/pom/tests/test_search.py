import allure
from src.pom.utility.coftest import GetDriver
from src.pom.pages.disclaimer_page import Disclaimer
from src.pom.pages.homepage_page import HomePage
from src.pom.pages.product_list_page import ProductList
from Data.data import Information


class TestSearch:

    driver = GetDriver().setUp()

    @allure.step("Search by a Keyword")
    def test_search(self):
        disc = Disclaimer(self.driver)
        disc.acceptDisclaimer()
        nav = HomePage(self.driver)
        nav.ourCategories()
        nav.search()
        nav.searchItem(Information.keyword)
        product = ProductList(self.driver)
        ProductName = product.returnFirstItemName()
        assert Information.keyword == ProductName
