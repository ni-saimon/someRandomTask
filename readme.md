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

https://github.com/ni-saimon/someRandomTask/assets/40791066/7fbf5cc3-39da-4638-be30-0e125bddb333



allure commandlines:

pytest --alluredir="./reports"

allure serve "./reports"
