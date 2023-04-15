from BaseApp import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class YandexSearchLocators:
    """A set of locators for interacting with the Yandex search page."""
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_IMAGES_HEADER = (By.XPATH, '/html/body/header/div/div[1]/div[2]/form/div[1]/span')
    LOCATOR_YANDEX_SEARCH_FIELD_TEXT = (By.ID, "value")
    LOCATOR_YANDEX_SUGGESTIONS = (By.CLASS_NAME, 'mini-suggest__popup-container')
    LOCATOR_YANDEX_FIRST_LINK = (By.XPATH, '/html/body/main/div[2]/div[2]/div/div[1]/ul/li[1]/div/div[1]/a')
    LOCATOR_YANDEX_PAGE_SOURCE = (By.XPATH, '//*[@id="search-result"]')
    LOCATOR_YANDEX_MENU_BUTTON = (By.XPATH, '/html/body/main/div[2]/form/div[2]/div/nav/ul/li[10]')
    LOCATOR_YANDEX_SCROLLBAR = (By.XPATH, '/html/body/div[4]')
    LOCATOR_YANDEX_POPULAR_IMAGES_FIRST = (By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div[1]')
    LOCATOR_YANDEX_IMAGE_BAR = (By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div')
    LOCATOR_YANDEX_MEDIA_VIEWER = (By.XPATH, "//div[contains(@class, 'MMImageWrapper')]")



class SearchHelper(BasePage):
    """Class for working with search queries."""

    def check_search_field(self):
        """Check search field."""
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)

    def get_images_header(self):
        """Get header for getting searching field."""
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_IMAGES_HEADER, time=3)

    def get_images_search_field(self, header):
        """Get images search field."""
        return header.find_element(By.XPATH, '/html/body/header/div/div[1]/div[2]/form/div[1]/span/span')

    def get_search_field_text(self, search_field):
        """Return search field text."""
        return search_field.get_attribute('value')

    def enter_word(self, search_field, word):
        """Enter word to the search field."""
        search_field.send_keys(word)
        return search_field

    def press_return_button(self, object):
        """Press Return button."""
        return object.send_keys(Keys.RETURN)

    def check_suggestions(self):
        """Check the suggestion."""
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SUGGESTIONS, time=10)

    def get_page_source(self):
        """Get the page source."""
        searching_results = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_PAGE_SOURCE, time=2)
        return len(searching_results)

    def check_first_link(self):
        """Check the first link."""
        first_link = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_FIRST_LINK)
        url = first_link.get_attribute(name='href')
        return url

    def check_menu_button(self):
        """Get the menu button."""
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_MENU_BUTTON)

    def get_scrollbar(self):
        """Get scrollar window, for getting service buttons."""
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SCROLLBAR, time=3)
    def get_images_button(self, scrollbar):
        """Get images page."""
        return scrollbar.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/div/div[3]/div[1]/span[9]')

    def get_first_popular_images_category(self):
        """Choose first popular image ."""
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_POPULAR_IMAGES_FIRST)

    @staticmethod
    def click_on(element):
        """Click on object."""
        return element.click()

    def switch_windows(self, number):
        """Switching browser window to next."""
        return self.go_to_window(number)

    def select_first_image(self, images):
        """Get first image from images search page."""
        return images.find_element(By.XPATH, "//div[contains(@class, 'item_first')]")
    def get_image_bar(self):
        """Get images bar."""
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_IMAGE_BAR, time=3)

    def get_media_viewer(self):
        """Get media viewer for checking image existing."""
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_MEDIA_VIEWER, time=3)

    def get_image(self, media_viewer):
        """Get image object."""
        return media_viewer.find_element(By.XPATH, "//img[contains(@class, 'MMImage-Preview')]")

    def next_button(self, media_viewer):
        """Switch image to next."""
        return media_viewer.find_element(By.XPATH, "//div[contains(@class, 'LayoutMain')]")

    def previous_button(self, media_viewer):
        """Switch image to previous."""
        return media_viewer.find_element(By.XPATH, "//div[contains(@class, 'MediaViewer-ButtonPrev')]")


