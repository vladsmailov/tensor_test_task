import sys
import time

from loguru import logger
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

logger.add(sys.stderr, format="{time} {level} {message}", colorize=True, filter="my_module", level="INFO") # noqa: 503
new_level = logger.level("START", no=38, color="<yellow>")


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://ya.ru/"

    @logger.catch
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    @logger.catch
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )

    @logger.catch
    def go_to_site(self):
        logger.log("START", "NEW SESSION STARTED.")
        return self.driver.get(self.base_url)

    @logger.catch
    def go_to_window(self, number):
        window = self.driver.window_handles[number]
        self.driver.switch_to.window(window)
        time.sleep(3)
        return

    @logger.catch
    def select_all_text(self):
        logger.info(
            "PRESSED BUTTON COMBINATION TO SELECT ALL TEXT IN TEXT AREA."
        )
        ActionChains(self.driver) \
            .key_down(Keys.CONTROL) \
            .send_keys('a') \
            .key_up(Keys.CONTROL) \
            .perform()

    @logger.catch
    def copy_all_text(self):
        logger.info(
            "PRESSED BUTTON COMBINATION TO COPY SELECTED TEXT IN CLIPBOARD."
        )
        ActionChains(self.driver) \
            .key_down(Keys.CONTROL) \
            .send_keys('c') \
            .key_up(Keys.CONTROL) \
            .perform()

    @logger.catch
    def press_escape(self):
        logger.info("PRESSED ESCAPE BUTTON.")
        ActionChains(self.driver).\
            send_keys(Keys.ESCAPE)\
            .perform()
