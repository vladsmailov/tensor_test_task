from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://ya.ru/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def go_to_window(self, number):
        window = self.driver.window_handles[number]
        return self.driver.switch_to.window(window)

    def select_all_text(self):
        ActionChains(self.driver) \
            .key_down(Keys.CONTROL) \
            .send_keys('a') \
            .key_up(Keys.CONTROL) \
            .perform()

    def copy_all_text(self):
        ActionChains(self.driver) \
            .key_down(Keys.CONTROL) \
            .send_keys('c') \
            .key_up(Keys.CONTROL) \
            .perform()

    def press_escape(self):
        ActionChains(self.driver).\
            send_keys(Keys.ESCAPE)\
            .perform()
