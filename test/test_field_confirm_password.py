import pytest
from page_object.registration import RegistrationFieldPasswordConfirm

@pytest.mark.parametrize("PASSWORD, CONFIRM_PASSWORD, ERROR_CONFIRM_PASSWORD, ERROR_CONFIRM_PASSWORD_one",
                         [('a1b2', 'a1b2', 'Пароль недостаточной длины (не может быть меньше 8 символа)', ''),
                          ('a1b2', '', 'Пароль недостаточной длины (не может быть меньше 8 символа)', 'Пароль не совпадает с подтверждением'),
                          ('', 'a1b2', 'Пароль недостаточной длины (не может быть меньше 8 символа)', 'Пароль не совпадает с подтверждением'),
                          ('12345678', '12345678', '', ''),
                          ('12345678', '', '', 'Пароль не совпадает с подтверждением'),
                          ('', '12345678', 'Пароль недостаточной длины (не может быть меньше 8 символа)', 'Пароль не совпадает с подтверждением'),
                          ('', '', 'Пароль недостаточной длины (не может быть меньше 8 символа)', '')
                          ])


def test_password_field(browser, PASSWORD, CONFIRM_PASSWORD, ERROR_CONFIRM_PASSWORD, ERROR_CONFIRM_PASSWORD_one):

    registration_page = RegistrationFieldPasswordConfirm(browser)
    registration_page.load_page()
    registration_page.input_password(PASSWORD)
    registration_page.input_confirm_password(CONFIRM_PASSWORD)
    registration_page.all_error_comment()

    # длинна пароля меньше 8-ми символов
    if len(PASSWORD) < 8 and PASSWORD == CONFIRM_PASSWORD:
        assert ERROR_CONFIRM_PASSWORD in registration_page.all_error_comment()
        assert ERROR_CONFIRM_PASSWORD_one not in registration_page.all_error_comment()

    elif len(PASSWORD) < 8 and len(PASSWORD) > len(CONFIRM_PASSWORD):
        assert ERROR_CONFIRM_PASSWORD in registration_page.all_error_comment()
        assert ERROR_CONFIRM_PASSWORD_one in registration_page.all_error_comment()

    #длинна пароля больше 8-ми символов
    elif len(PASSWORD) > 7 and PASSWORD == CONFIRM_PASSWORD:
        assert ERROR_CONFIRM_PASSWORD not in registration_page.all_error_comment()
        assert ERROR_CONFIRM_PASSWORD_one not in registration_page.all_error_comment()

    elif len(PASSWORD) > 7 and len(PASSWORD) > len(CONFIRM_PASSWORD):
        assert ERROR_CONFIRM_PASSWORD not in registration_page.all_error_comment()
        assert ERROR_CONFIRM_PASSWORD_one in registration_page.all_error_comment()

    elif len(PASSWORD) > 7 and len(PASSWORD) < len(CONFIRM_PASSWORD):
        assert ERROR_CONFIRM_PASSWORD in registration_page.all_error_comment()
        assert ERROR_CONFIRM_PASSWORD_one in registration_page.all_error_comment()

    elif len(PASSWORD) > 7 and PASSWORD == '' and CONFIRM_PASSWORD == '':
        assert ERROR_CONFIRM_PASSWORD in registration_page.all_error_comment()
        assert ERROR_CONFIRM_PASSWORD_one not in registration_page.all_error_comment()

    # поля должны быть пустыми
    assert registration_page.password_value() == ''
    assert registration_page.confirm_password_value() == ''