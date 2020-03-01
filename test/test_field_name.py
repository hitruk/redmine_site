import pytest
from page_object.registration import RegistrationFieldName


@pytest.mark.parametrize("NAME, ERROR_NAME", [('andrey', '')])
def tests_name(browser, NAME, ERROR_NAME):

    registration_page = RegistrationFieldName(browser)
    registration_page.load_page()
    registration_page.input_name(NAME)

    if ERROR_NAME != '':
        assert registration_page.error_name_comment(ERROR_NAME) == ERROR_NAME
    else:
        assert registration_page.error_comments() == 4

    assert registration_page.name_field_value() == NAME  # имя не сбрасывается



