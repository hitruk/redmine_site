import pytest
from page_object.registration import RegistrationFieldPassword

# Пароль недостаточной длины (не может быть меньше 8 символа)
@pytest.mark.parametrize("PASSWORD, ERROR_PASSWORD", [('12345', 'Пароль недостаточной длины (не может быть меньше 8 символа)')])
def test_password(browser, PASSWORD, ERROR_PASSWORD):

    registration_page = RegistrationFieldPassword(browser)
    registration_page.load_page()
    registration_page.input_password(PASSWORD)

    if ERROR_PASSWORD != '':
        assert registration_page.error_password_comment(ERROR_PASSWORD) == ERROR_PASSWORD
    else:
        assert registration_page.error_comments() == 4

    assert registration_page.field_value() == '' # пароль сбрасывается