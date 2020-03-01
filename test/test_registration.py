import pytest
from selenium.webdriver.common.keys import Keys


@pytest.mark.parametrize("LOGIN, PASSWORD, CONFIRM_PASSWORD, FIRSTNAME, LASTNAME, EMAIL",
                         [()])
def test_registration(browser, LOGIN, PASSWORD, CONFIRM_PASSWORD, FIRSTNAME, LASTNAME, EMAIL):

    URL = ''
    browser.get(URL)

    input_login = browser.find_element_by_id('user_login')
    input_login.send_keys(LOGIN)

    input_password = browser.find_element_by_id('user_password')
    input_password.send_keys(PASSWORD)

    input_confirm_password = browser.find_element_by_id('user_password_confirmation')
    input_confirm_password.send_keys(CONFIRM_PASSWORD)

    input_name = browser.find_element_by_id('user_firstname')
    input_name.send_keys(FIRSTNAME)

    input_lastname = browser.find_element_by_id('user_lastname')
    input_lastname.send_keys(LASTNAME)

    input_email = browser.find_element_by_id('user_mail')
    input_email.send_keys(EMAIL+Keys.RETURN)





