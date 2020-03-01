
import pytest
from page_object.registration import RegistrationFieldEmail

@pytest.mark.parametrize("EMAIL, ERROR_EMAIL", [('jhdf','Email имеет неверное значение'), ('joo@mail.ru','')])
def test_mail(browser, EMAIL, ERROR_EMAIL):

    registration_page = RegistrationFieldEmail(browser)
    registration_page.load_page()
    registration_page.input_email(EMAIL)

    if ERROR_EMAIL != '':
        assert registration_page.error_email_comment(ERROR_EMAIL) == ERROR_EMAIL
    else:
        assert registration_page.error_comments() == 4

    assert registration_page.email_value() == EMAIL