import pytest

# from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
import psycopg2

# browser
@pytest.fixture
def browser():
    driver = Firefox(executable_path='/home/hitruk/dir/geckodriver')
    # driver = Chrome(executable_path='/home/hitruk/dir/chromedriver')

    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# database
@pytest.fixture
def database():
    @pytest.fixture
    def database():
        cnx = psycopg2.connect(user='redmine', password='q1w2', database='redmine', host='192.168.100.16')
        cursor = cnx.cursor()
        yield cursor
        # cnx.commit()
        cursor.close()
        cnx.close()