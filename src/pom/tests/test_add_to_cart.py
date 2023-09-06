import allure
import unittest
from src.pom.utility.coftest import GetDriver
from src.pom.pages.disclaimer_page import Disclaimer
from src.pom.pages.navigation_drawer_page import NavigationDrawer
from src.pom.pages.category_page import Category
from src.pom.pages.product_list_page import ProductList
from src.pom.pages.product_details_page import ProductDetails


class TestAddToCart(unittest.TestCase):

    driver = GetDriver().setUp()

    @allure.step("Add to Cart")
    def test_navigation_drawer(self):
        disc = Disclaimer(self.driver)
        disc.acceptDisclaimer()
        nav = NavigationDrawer(self.driver)
        nav.category()
        elec = Category(self.driver)
        elec.electronics()
        nav.search()
        nav.searchItem("Mattress Bedroom")
        product = ProductList(self.driver)
        product.firstItem()
        cart = ProductDetails(self.driver)
        cart.checkWishlistButtonAvailable()
        cart.increaseQuantityByOne()
        cart.addToCart()
        cart.navigateToCart()
