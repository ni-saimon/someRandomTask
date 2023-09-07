import allure
from src.pom.utility.coftest import GetDriver
from src.pom.pages.disclaimer_page import Disclaimer
from src.pom.pages.homepage_page import HomePage
from src.pom.pages.product_list_page import ProductList
from src.pom.pages.product_details_page import ProductDetails
from src.pom.pages.cart_page import Checkout
from Data.data import Information


class TestCheckoutAsGuest:

    driver = GetDriver().setUp()

    @allure.step("Checkout As a Guest")
    def test_checkout_as_guest(self):
        disc = Disclaimer(self.driver)
        disc.acceptDisclaimer()
        nav = HomePage(self.driver)
        nav.ourCategories()
        nav.search()
        nav.searchItem(Information.keyword)
        product = ProductList(self.driver)
        product.firstItem()
        cart = ProductDetails(self.driver)
        cart.checkWishlistButtonAvailable()
        cart.increaseQuantityByOne()
        cart.addToCart()
        cart.navigateToCart()
        checkout = Checkout(self.driver)
        checkout.checkout()
        checkout.guestCheckout()
