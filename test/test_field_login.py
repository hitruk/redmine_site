import pytest
from page_object.registration import RegistrationFieldLogin


@pytest.mark.parametrize("LOGIN, ERROR_LOGIN", [('user', '')])
def test_login(browser, LOGIN, ERROR_LOGIN):

    registration_page = RegistrationFieldLogin(browser)
    registration_page.load_page()
    registration_page.input_login(LOGIN)

    if ERROR_LOGIN != '':
        assert registration_page.error_login_comment(ERROR_LOGIN) == ERROR_LOGIN
    else:
        assert registration_page.error_comments() == 4

    assert registration_page.login_field_value() == LOGIN