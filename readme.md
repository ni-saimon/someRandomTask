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

Order test video:


https://github.com/ni-saimon/someRandomTask/assets/40791066/0b4273bc-224b-4bbc-9abb-796d4a5b309e


allure commandlines:

pytest --alluredir="./reports"

allure serve "./reports"
