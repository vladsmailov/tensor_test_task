import pytest
from selenium import webdriver

from yandex_pages import SearchHelper


@pytest.fixture(scope="session")
def yandex_page():
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    main_page = SearchHelper(driver)
    main_page.go_to_site()
    yield main_page
    driver.quit()
