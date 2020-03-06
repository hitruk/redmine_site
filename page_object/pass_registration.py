from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class RegistrationPage:

    URL = 'https://192.168.1.3/redmine/account/register'

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)


class PassRegistration(RegistrationPage):

    INPUT_LOGIN = (By.ID, 'user_login')
    INPUT_PASSWORD = (By.ID, 'user_password')
    INPUT_CONFIRM_PASSWORD = (By.ID, 'user_password_confirmation')
    INPUT_FIRSTNAME = (By.ID, 'user_firstname')
    INPUT_LASTNAME = (By.ID, 'user_lastname')
    INPUT_EMAIL = (By.ID, 'user_mail')
    ALL_COMMENT_ERROR = (By.CSS_SELECTOR, '#errorExplanation>ul>li')


    def input_all_data(self, login, password, confirn_password, firstname, lastname, email):

        input_login = self.browser.find_element(*self.INPUT_LOGIN)
        input_login.send_keys(login)
        input_password = self.browser.find_element(*self.INPUT_PASSWORD)
        input_password.send_keys(password)
        input_confirm_password = self.browser.find_element(*self.INPUT_CONFIRM_PASSWORD)
        input_confirm_password.send_keys(confirn_password)
        input_firstname = self.browser.find_element(*self.INPUT_FIRSTNAME)
        input_firstname.send_keys(firstname)
        input_lastname = self.browser.find_element(*self.INPUT_LASTNAME)
        input_lastname.send_keys(lastname)
        input_email = self.browser.find_element(*self.INPUT_EMAIL)
        input_email.send_keys(email+Keys.RETURN)

    def all_error_commments(self):
        list_error_comments = []  # список сообщений об ошибках
        error_comments = self.browser.find_elements(*self.ALL_COMMENT_ERROR)
        for row in error_comments:
            list_error_comments.append(row.text)
        return len(list_error_comments)