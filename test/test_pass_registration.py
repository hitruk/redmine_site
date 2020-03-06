import pytest
from page_object.pass_registration import PassRegistration
from page_object.result_registration import ResultRegistration


@pytest.mark.parametrize("LOGIN, PASSWORD, CONFIRM_PASSWORD, FIRSTNAME, LASTNAME, EMAIL",
                         [('user_one', 'a_12345678', 'a_12345678', 'Peter', 'Sokolov', 'sokolov@gmail.com'),
                          ('', 'a_12345678', 'a_12345678', 'Peter', 'Sokolov', 'sokolov@gmail.com')
                          ])


def test_registration(browser, database, LOGIN, PASSWORD, CONFIRM_PASSWORD, FIRSTNAME, LASTNAME, EMAIL):

    registration_page = PassRegistration(browser)
    registration_page.load_page()
    registration_page.input_all_data(LOGIN, PASSWORD, CONFIRM_PASSWORD, FIRSTNAME, LASTNAME, EMAIL)

    if registration_page.all_error_commments() == 0:

        result_page = ResultRegistration(browser, database)

        assert result_page.result_registration_comment() == 'Ваша учётная запись создана и ожидает подтверждения администратора.'
        assert result_page.data_db(LOGIN)[0] == LOGIN
        assert result_page.data_db(LOGIN)[1] == FIRSTNAME
        assert result_page.data_db(LOGIN)[2] == LASTNAME
        assert result_page.data_email_db(EMAIL) == EMAIL

        # очищаем таблицы в базе данных, таблица users, data
        result_page.clear_table_users(LOGIN)
        result_page.clear_table_email_addresses(EMAIL)

    else:
        assert registration_page.all_error_commments() > 0