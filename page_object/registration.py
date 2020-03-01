from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class RegistrationPage:

    URL = 'https://192.168.1.3/redmine/account/register'

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)


class RegistrationFieldLogin(RegistrationPage):

    INPUT_LOGIN = (By.ID, 'user_login')
    LOGIN_FIELD_VALUE = (By.ID, 'user_login')
    ERROR_COMMENTS = (By.CSS_SELECTOR, '#errorExplanation>ul>li')

    @classmethod
    def ERROR_LOGIN_COMMENT(cls, error_login):
        xpath = f"//div[@id='errorExplanation']/ul//li[contains(text(), '{error_login}')]"
        return (By.XPATH, xpath)

    def input_login(self, login):
        login_input = self.browser.find_element(*self.INPUT_LOGIN)
        login_input.send_keys(login+Keys.RETURN)

    def error_login_comment(self, error_login):
        login_error = self.browser.find_element(*self.ERROR_LOGIN_COMMENT(error_login))
        return login_error.text

    def error_comments(self):
        comments_error = self.browser.find_elements(*self.ERROR_COMMENTS)
        return len(comments_error)

    def login_field_value(self):
        field_login_value = self.browser.find_element(*self.LOGIN_FIELD_VALUE)
        return field_login_value.get_attribute('value')


class RegistrationFieldPassword(RegistrationPage):

    INPUT_PASSWORD = (By.ID, 'user_password')

    @classmethod
    def ERROR_LOGIN_COMMENT(cls, error_password):
        xpath = f"//div[@id='errorExplanation']/ul//li[contains(text(), '{error_password}')]"
        return (By.XPATH, xpath)

    ERROR_COMMENTS = (By.CSS_SELECTOR, '#errorExplanation>ul>li')
    PASSWORD_VALUE = (By.ID, 'user_password')

    def input_password(self, password):
        input_password = self.browser.find_element(*self.INPUT_PASSWORD)
        input_password.send_keys(password+Keys.RETURN)

    def error_password_comment(self, error_password):
        login_error = self.browser.find_element(*self.ERROR_LOGIN_COMMENT(error_password))
        return login_error.text

    def error_comments(self):
        comments_error = self.browser.find_elements(*self.ERROR_COMMENTS)
        return len(comments_error)

    def field_value(self):
        value_password = self.browser.find_element(*self.INPUT_PASSWORD)
        return value_password.get_attribute('value')

# необходимо реализовать/Реализовываем
class RegistrationFieldPasswordConfirm(RegistrationPage):

    INPUT_PASSWORD = (By.ID, 'user_password')
    INPUT_CONFIRM_PASSWORD = (By.ID, 'user_password_confirmation')
    ALL_ERROR_COMMENTS = (By.CSS_SELECTOR, '#errorExplanation>ul>li')
    PASSWORD_VALUE = (By.ID, 'user_password')
    CONFIRM_PASSWORD_VALUE = (By.ID, 'user_password_confirmation')

    def input_password(self, password):
        password_input = self.browser.find_element(*self.INPUT_PASSWORD)
        password_input.send_keys(password)

    def input_confirm_password(self, confirm_password):
        input_password_confirm = self.browser.find_element(*self.INPUT_CONFIRM_PASSWORD)
        input_password_confirm.send_keys(confirm_password+Keys.RETURN)

    def all_error_comment(self):
        list_error_comments = []  # список всех сообщений об ошибках
        all_comment_error = self.browser.find_elements(*self.ALL_ERROR_COMMENTS)
        for row in all_comment_error:
            list_error_comments.append(row.text)
        return list_error_comments

    def password_value(self):
        value_password = self.browser.find_element(*self.INPUT_PASSWORD)
        return value_password.get_attribute('value')

    def confirm_password_value(self):
        value_confirm_password = self.browser.find_element(*self.CONFIRM_PASSWORD_VALUE)
        return value_confirm_password.get_attribute('value')


class RegistrationFieldName(RegistrationPage):

    INPUT_NAME = (By.ID, 'user_firstname')

    @classmethod
    def ERROR_NAME_COMMENT(cls, error_name):
        xpath = f"//div[@id='errorExplanation']/ul//li[contains(text(), '{error_name}')]"
        return (By.XPATH, xpath)

    ERROR_COMMENTS = (By.CSS_SELECTOR, '#errorExplanation>ul>li')
    NAME_FIELD_VALUE = (By.ID, 'user_firstname')

    def input_name(self, name):
        name_input = self.browser.find_element(*self.INPUT_NAME)
        name_input.send_keys(name+Keys.RETURN)

    def error_name_comment(self, error_name):
        login_error = self.browser.find_element(*self.ERROR_NAME_COMMENT(error_name))
        return login_error.text

    def error_comments(self):
        comments_error = self.browser.find_elements(*self.ERROR_COMMENTS)
        return len(comments_error)

    def name_field_value(self):
        field_name = self.browser.find_element(*self.NAME_FIELD_VALUE)
        return field_name.get_attribute('value')


class RegistrationFieldLastname(RegistrationPage):

        INPUT_LASTNAME = (By.ID, 'user_lastname')

        @classmethod
        def ERROR_LASTNAME_COMMENT(cls, error_lastname):
            xpath = f"//div[@id='errorExplanation']/ul//li[contains(text(), '{error_lastname}')]"
            return (By.XPATH, xpath)

        LASTNAME_FIELD_VALUE = (By.ID, 'user_lastname')
        ERROR_COMMENTS = (By.CSS_SELECTOR, '#errorExplanation>ul>li')

        def input_lastname(self, lastname):
            lastname_input = self.browser.find_element(*self.INPUT_LASTNAME)
            lastname_input.send_keys(lastname+Keys.RETURN)

        def error_lastname_comment(self, error_lastname):
            lastname_error_comment = self.browser.find_element(*self.ERROR_LASTNAME_COMMENT(error_lastname))
            return lastname_error_comment.text

        def error_comments(self):
            comments_error = self.browser.find_elements(*self.ERROR_COMMENTS)
            return len(comments_error)

        def lastname_field_value(self):
            field_lastname = self.browser.find_element(*self.LASTNAME_FIELD_VALUE)
            return field_lastname.get_attribute('value')


class RegistrationFieldEmail(RegistrationPage):

    INPUT_EMAIL = (By.ID, 'user_mail')

    @classmethod
    def ERROR_EMAIL_COMMENT(cls, error_email):
        xpath = f"//div[@id='errorExplanation']/ul//li[contains(text(), '{error_email}')]"
        return (By.XPATH, xpath)

    ERROR_COMMENTS = (By.CSS_SELECTOR, '#errorExplanation>ul>li')
    EMAIL_VALUE = (By.ID, 'user_mail')

    def input_email(self, email):
        email_input = self.browser.find_element(*self.INPUT_EMAIL)
        email_input.send_keys(email+Keys.RETURN)

    def error_email_comment(self, error_email):
        email_error_comment = self.browser.find_element(*self.ERROR_EMAIL_COMMENT(error_email))
        return email_error_comment.text

    def error_comments(self):
        comments_error = self.browser.find_elements(*self.ERROR_COMMENTS)
        return len(comments_error)

    def email_value(self):
        value_email = self.browser.find_element(*self.EMAIL_VALUE)
        return value_email.get_attribute('value')






