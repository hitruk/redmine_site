import pytest
from selenium.webdriver.common.keys import Keys
import time

@pytest.mark.parametrize("LOGIN, PASSWORD, CONFIRM_PASSWORD, FIRSTNAME, LASTNAME, EMAIL",
                         [('user_one', 'a_12345678', 'a_12345678', 'Peter', 'Sokolov', 'sokolov@gmail.com'),
                          ('', 'a_12345678', 'a_12345678', 'Peter', 'Sokolov', 'sokolov@gmail.com')
                          ])

def test_registration(browser, database, LOGIN, PASSWORD, CONFIRM_PASSWORD, FIRSTNAME, LASTNAME, EMAIL):

    URL = 'https://192.168.1.3/redmine/account/register'
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

    list_error_comments = []  # список всех сообщений об ошибках
    all_comment_error = browser.find_elements_by_css_selector('#errorExplanation>ul>li')
    for row in all_comment_error:
        list_error_comments.append(row.text)

    if len(list_error_comments) == 0:
        result_registration_comment = browser.find_element_by_id('flash_error')
        assert result_registration_comment.text == 'Ваша учётная запись создана и ожидает подтверждения администратора.'


        # f"SELECT login, firstname, lastname FROM users WHERE login = '{LOGIN}'"
        database.execute(f"SELECT login, firstname, lastname FROM users WHERE login = '{LOGIN}'")
        login_db = database.fetchone()
        assert login_db[0] == LOGIN
        assert login_db[1] == FIRSTNAME
        assert login_db[2] == LASTNAME

        database.execute(f"SELECT address FROM email_addresses WHERE address = '{EMAIL}'")
        email_db = database.fetchone()
        assert email_db[0] == EMAIL

        # очищаем db
        database.execute(f"DELETE FROM users WHERE login = '{LOGIN}'")
        database.execute(f"DELETE FROM email_addresses WHERE address = '{EMAIL}'")

    else:
        assert len(list_error_comments) > 0

