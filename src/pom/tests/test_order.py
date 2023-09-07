import allure
from src.pom.utility.coftest import GetDriver
from src.pom.pages.disclaimer_page import Disclaimer
from src.pom.pages.homepage_page import HomePage
from src.pom.pages.product_list_page import ProductList
from src.pom.pages.product_details_page import ProductDetails
from src.pom.pages.cart_page import Checkout
from src.pom.pages.address_page import FillUpAddress
from src.pom.pages.deliverytype_page import ShipmentType
from src.pom.pages.payment_page import PaymentType
from src.pom.pages.orderconfirmation_page import OrderFinalize
from Data.data import Information


class TestOrderAsGuest:

    driver = GetDriver().setUp()

    @allure.step("Complete an Order")
    def test_order(self):
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
        order = FillUpAddress(self.driver)
        order.customerInformation()
        shipping = ShipmentType(self.driver)
        shipping.shippingNextDayAir()
        pay = PaymentType(self.driver)
        pay.checkMoneyOrderPayment()
        placeOrder = OrderFinalize(self.driver)
        message = placeOrder.orderSuccessful()
        assert Information.successMessage in message
