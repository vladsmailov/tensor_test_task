import sys

from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base_app import BasePage

logger.add(sys.stderr, format="{time} {level} {message}", colorize=True, filter="my_module", level="INFO") # noqa: 503
logger.add("log_file.log", level="TRACE", rotation="5 MB")


class YandexSearchLocators:
    """A set of locators for interacting with the Yandex search page."""
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_IMAGES_HEADER = (
        By.XPATH, '/html/body/header/div/div[1]/div[2]/form/div[1]/span'
    )
    LOCATOR_YANDEX_SEARCH_FIELD_TEXT = (By.ID, "value")
    LOCATOR_YANDEX_SUGGESTIONS = (
        By.CLASS_NAME, 'mini-suggest__popup-container'
    )
    LOCATOR_YANDEX_FIRST_LINK = (
        By.XPATH,
        '/html/body/main/div[2]/div[2]/div/div[1]/ul/li[1]/div/div[1]/a'
    )
    LOCATOR_YANDEX_PAGE_SOURCE = (By.XPATH, '//*[@id="search-result"]')
    LOCATOR_YANDEX_MENU_BUTTON = (
        By.XPATH, '/html/body/main/div[2]/form/div[2]/div/nav/ul/li[10]'
    )
    LOCATOR_YANDEX_SCROLLBAR = (By.XPATH, '/html/body/div[4]')
    LOCATOR_YANDEX_POPULAR_IMAGES_FIRST = (
        By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div[1]'
    )
    LOCATOR_YANDEX_IMAGE_BAR = (
        By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div'
    )
    LOCATOR_YANDEX_MEDIA_VIEWER = (
        By.XPATH, "//div[contains(@class, 'MMImageWrapper')]"
    )


class SearchHelper(BasePage):
    """Class for working with search queries."""

    @logger.catch
    def get_search_field(self):
        """Check search field."""
        logger.info("SEARCH FIELD OBJECT RECIEVED.")
        return self.find_element(
            YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD, time=3
        )

    @logger.catch
    def get_images_header(self):
        """Get header for getting searching field."""
        logger.info("HEADER OBJECT ON THE IMAGE SEARCHING FIELD RECIEVED.")
        return self.find_element(
            YandexSearchLocators.LOCATOR_YANDEX_IMAGES_HEADER, time=3
        )

    @logger.catch
    def get_images_search_field(self, header):
        """Get images search field."""
        logger.info("IMAGE SEARCH FIELD RECIEVED.")
        return header.find_element(
            By.XPATH,
            '/html/body/header/div/div[1]/div[2]/form/div[1]/span/span'
        )

    @logger.catch
    def get_search_field_text(self, search_field):
        """Get search field text."""
        logger.info(
            f"SEARCH FIELD TEXT={search_field.get_attribute('value')}."
        )
        return search_field.get_attribute('value')

    @logger.catch
    def enter_word(self, search_field, word):
        """Enter word to the search field."""
        logger.info(f"TEXT={word} TYPED INTO SEARCH FIELD.")
        search_field.send_keys(word)
        return search_field

    @logger.catch
    def press_return_button(self, object):
        """Press Return button."""
        logger.info("RETURN BUTTON PRESSED.")
        return object.send_keys(Keys.RETURN)

    @logger.catch
    def get_suggestions(self):
        """Check the suggestion."""
        logger.info("SUGGESTIONS IN SEARCH FIELD RECIEVED.")
        return self.find_element(
            YandexSearchLocators.LOCATOR_YANDEX_SUGGESTIONS, time=10
        )

    @logger.catch
    def get_page_source(self):
        """Get the page source."""
        logger.info("PAGE SOURCE RECIEVED.")
        searching_results = self.find_elements(
            YandexSearchLocators.LOCATOR_YANDEX_PAGE_SOURCE, time=2
        )
        return len(searching_results)

    @logger.catch
    def get_first_link(self):
        """Get the first link."""
        first_link = self.find_element(
            YandexSearchLocators.LOCATOR_YANDEX_FIRST_LINK, time=3
        )
        url = first_link.get_attribute(name='href')
        logger.info(f"FIRST LINK IN THE SEARCHING RESULT: {url}.")
        return url

    @logger.catch
    def get_menu_button(self):
        """Get the menu button."""
        logger.info("MENU BUTTON RECIEVED.")
        return self.find_element(
            YandexSearchLocators.LOCATOR_YANDEX_MENU_BUTTON, time=3
        )

    @logger.catch
    def get_scrollbar(self):
        """Get scrollar window, for getting service buttons."""
        logger.info("SCROLLBAR RECIEVED.")
        return self.find_element(
            YandexSearchLocators.LOCATOR_YANDEX_SCROLLBAR, time=3
        )

    @logger.catch
    def get_images_button(self, scrollbar):
        """Get images page."""
        logger.info("IMAGES BUTTON RECIEVED.")
        return scrollbar.find_element(
            By.XPATH, "//a[contains(@href, 'https://yandex.ru/images/')]"
        )

    @logger.catch
    def get_first_popular_images_category(self):
        """Choose first popular image ."""
        logger.info("FIRST POPULAR IMAGES CATEGORY RECIEVED.")
        return self.find_element(
            YandexSearchLocators.LOCATOR_YANDEX_POPULAR_IMAGES_FIRST, time=5
        )

    @staticmethod
    def click_on(element):
        """Click on object."""
        logger.info("MOUSE LEFT CLICK.")
        return element.click()

    @logger.catch
    def switch_windows(self, number):
        """Switching browser window to next."""
        logger.info("BROWSER TAB WAS SWITCHED.")
        return self.go_to_window(number)

    @logger.catch
    def select_first_image(self, images):
        """Get first image from images search page."""
        logger.info("FIRST IMAGE FROM IMAGES-SEARCH RESULT RECIEVED.")
        return images.find_element(
            By.XPATH, "//div[contains(@class, 'item_first')]"
        )

    @logger.catch
    def get_image_bar(self):
        """Get images bar."""
        logger.info("IMAGES BAR RECIEVED.")
        return self.find_element(
            YandexSearchLocators.LOCATOR_YANDEX_IMAGE_BAR, time=3
        )

    @logger.catch
    def get_media_viewer(self):
        """Get media viewer for checking image existing."""
        logger.info("MEDIA VIEWER RECIEVED.")
        return self.find_element(
            YandexSearchLocators.LOCATOR_YANDEX_MEDIA_VIEWER, time=3
        )

    @logger.catch
    def get_image(self, media_viewer):
        """Get image object."""
        logger.info("IMAGE PREVIEW OBJECT RECIEVED.")
        return media_viewer.find_element(
            By.XPATH, "//img[contains(@class, 'MMImage-Preview')]"
        )

    @logger.catch
    def next_button(self, media_viewer):
        """Switch image to next."""
        logger.info("MEDIA VIEWER NEXT IMAGE BUTTON RECIEVED.")
        return media_viewer.find_element(
            By.XPATH, "//div[contains(@class, 'LayoutMain')]"
        )

    @logger.catch
    def previous_button(self, media_viewer):
        """Switch image to previous."""
        logger.info("MEDIA VIEWER PREVIOUS IMAGE BUTTON RECIEVED.")
        return media_viewer.find_element(
            By.XPATH, "//div[contains(@class, 'MediaViewer-ButtonPrev')]"
        )

    @logger.catch
    def get_url(self):
        """Get url of current page."""
        logger.info(f"CURRENT URL RECIEVED: {self.driver.current_url}.")
        return self.driver.current_url
