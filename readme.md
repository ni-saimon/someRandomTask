order placement as a guest using appium python

-all tests:
    accept disclaimer;
    homepage;
    search;
    add to cart;
    checkout;
    order placement;

-used allure report for reporting

-parsed guest information, quantity, product name, confirmation message from csv



allure commandlines:

pytest --alluredir="./reports"

allure serve "./reports"