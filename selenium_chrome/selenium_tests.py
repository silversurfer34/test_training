from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest


@pytest.fixture
def driver():
    _driver = driver = webdriver.Chrome()
    yield _driver
    _driver.close()


def test_search_in_python_org(driver):
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.send_keys("pytest")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source


def test_fail_search_in_python_org(driver):
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.send_keys("totototo")
    elem.send_keys(Keys.RETURN)
    assert "No results found." in driver.page_source