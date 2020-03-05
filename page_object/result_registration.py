from selenium.webdriver.common.by import By


class ResultRegistration:


    # ALL_COMMENT_ERROR = (By.CSS_SELECTOR, '#errorExplanation>ul>li')
    RESULT_RGISTRATION_COMMENT = (By.ID, 'flash_error')


    def __init__(self, browser, database):
        self.browser = browser
        self.database = database

    def result_registration_comment(self):

        result_registration_comment = self.browser.find_element(*self.RESULT_RGISTRATION_COMMENT)
        return result_registration_comment.text

    def data_db(self, login):
        SQL = f"SELECT login, firstname, lastname FROM users WHERE login = '{login}'"
        self.database.execute(SQL)
        db_data = self.database.fetchone()
        return db_data

    def data_email_db(self, email):
        SQL = f"SELECT address FROM email_addresses WHERE address = '{email}'"
        self.database.execute(SQL)
        email_db = self.database.fetchone()
        return email_db[0]

    def clear_table_users(self, login):
        SQL = f"DELETE FROM users WHERE login = '{login}'"
        db_clear = self.database.execute(SQL)
        return db_clear

    def clear_table_email_addresses(self, email):
        SQl = f"DELETE FROM email_addresses WHERE address = '{email}'"
        db_clear = self.database.execute(SQl)
        return db_clear

