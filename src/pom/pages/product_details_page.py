from appium.webdriver.common.appiumby import AppiumBy
from src.pom.pages.base_page import BasePage
from src.pom.locators.product_details_page import Locators


class ProductDetails(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super(ProductDetails, self).__init__(driver)

    plusBtn = (AppiumBy.ID, Locators.btnPlus)
    addToCartBtn = (AppiumBy.ID, Locators.btnAddToCart)
    wishlistBtn = (AppiumBy.ID, Locators.fabAddToWishlist)
    cartBtn = (AppiumBy.ID, Locators.counterIcon)

    def checkWishlistButtonAvailable(self):
        self.wait_for_clickable(self.wishlistBtn)

    def increaseQuantityByOne(self):
        self.swipeDown()
        self.click(self.plusBtn)

    def addToCart(self):
        self.click(self.addToCartBtn)

    def navigateToCart(self):
        self.click(self.cartBtn)
