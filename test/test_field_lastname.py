import pytest
from page_object.registration import RegistrationFieldLastname


@pytest.mark.parametrize("LASTNAME, ERROR_LASTNAME", [('hitruk', '')])
def test_lastname(browser, LASTNAME, ERROR_LASTNAME):

    registration_page = RegistrationFieldLastname(browser)
    registration_page.load_page()
    registration_page.input_lastname(LASTNAME)

    if ERROR_LASTNAME != '':
        assert registration_page.error_lastname_comment(ERROR_LASTNAME) == ERROR_LASTNAME
    else:
        assert registration_page.error_comments() == 4

    assert registration_page.lastname_field_value() == LASTNAME