import time
import tkinter as tk

from YandexPages import SearchHelper


def test_yandex_image_search_menu_button_existing(browser):
    """Menu button existing check."""
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.check_search_field()
    menu_button = yandex_main_page.check_menu_button()
    assert menu_button is not None

def test_yandex_image_search_image_page(browser):
    """Checking the transition to the page 'https://yandex.ru/images/'."""
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    search_field = yandex_main_page.check_search_field()
    yandex_main_page.click_on(search_field)
    menu_button = yandex_main_page.check_menu_button()
    yandex_main_page.click_on(menu_button)
    scrollbar = yandex_main_page.get_scrollbar()
    images_button = yandex_main_page.get_images_button(scrollbar)
    yandex_main_page.click_on(images_button)
    yandex_main_page.switch_windows(-1)
    time.sleep(3)
    url = browser.current_url
    assert url == 'https://yandex.ru/images/'

def test_yandex_image_search_check_search_field_text(browser):
    """Checking the opening of the first image."""
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    search_field = yandex_main_page.check_search_field()
    yandex_main_page.click_on(search_field)
    menu_button = yandex_main_page.check_menu_button()
    yandex_main_page.click_on(menu_button)
    scrollbar = yandex_main_page.get_scrollbar()
    images_button = yandex_main_page.get_images_button(scrollbar)
    yandex_main_page.click_on(images_button)
    yandex_main_page.switch_windows(-1)
    time.sleep(3)
    first_popular_images_category = yandex_main_page.get_first_popular_images_category()
    yandex_main_page.click_on(first_popular_images_category)
    header = yandex_main_page.get_images_header()
    search_field = yandex_main_page.get_images_search_field(header)
    time.sleep(3)
    yandex_main_page.click_on(search_field)
    yandex_main_page.select_all_text()
    time.sleep(3)
    yandex_main_page.copy_all_text()
    time.sleep(3)
    root = tk.Tk()
    text = root.clipboard_get()
    assert text is not None

def test_yandex_image_search_image_opening(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    search_field = yandex_main_page.check_search_field()
    yandex_main_page.click_on(search_field)
    menu_button = yandex_main_page.check_menu_button()
    yandex_main_page.click_on(menu_button)
    scrollbar = yandex_main_page.get_scrollbar()
    images_button = yandex_main_page.get_images_button(scrollbar)
    yandex_main_page.click_on(images_button)
    yandex_main_page.switch_windows(-1)
    time.sleep(3)
    first_popular_images_category = yandex_main_page.get_first_popular_images_category()
    yandex_main_page.click_on(first_popular_images_category)
    time.sleep(3)
    images = yandex_main_page.get_image_bar()
    first_image = yandex_main_page.select_first_image(images)
    time.sleep(3)
    yandex_main_page.click_on(first_image)
    time.sleep(3)
    media_viewer = yandex_main_page.get_media_viewer()
    image = yandex_main_page.get_image(media_viewer)
    assert image.get_attribute('class') == 'MMImage-Preview'

def test_yandex_image_search_image_changing(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    search_field = yandex_main_page.check_search_field()
    yandex_main_page.click_on(search_field)
    menu_button = yandex_main_page.check_menu_button()
    yandex_main_page.click_on(menu_button)
    scrollbar = yandex_main_page.get_scrollbar()
    images_button = yandex_main_page.get_images_button(scrollbar)
    yandex_main_page.click_on(images_button)
    yandex_main_page.switch_windows(-1)
    time.sleep(3)
    first_popular_images_category = yandex_main_page.get_first_popular_images_category()
    yandex_main_page.click_on(first_popular_images_category)
    time.sleep(3)
    images = yandex_main_page.get_image_bar()
    first_image = yandex_main_page.select_first_image(images)
    time.sleep(3)
    yandex_main_page.click_on(first_image)
    time.sleep(3)
    media_viewer = yandex_main_page.get_media_viewer()
    first_image_preview = yandex_main_page.get_image(media_viewer)
    first_image_src = first_image_preview.get_attribute('src')
    button = yandex_main_page.next_button(media_viewer)
    yandex_main_page.click_on(button)
    second_image_preview = yandex_main_page.get_image(media_viewer)
    second_image_src = second_image_preview.get_attribute('src')
    assert first_image_src != second_image_src

def test_yandex_image_search_image_return(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    search_field = yandex_main_page.check_search_field()
    yandex_main_page.click_on(search_field)
    menu_button = yandex_main_page.check_menu_button()
    yandex_main_page.click_on(menu_button)
    scrollbar = yandex_main_page.get_scrollbar()
    images_button = yandex_main_page.get_images_button(scrollbar)
    yandex_main_page.click_on(images_button)
    yandex_main_page.switch_windows(-1)
    time.sleep(3)
    first_popular_images_category = yandex_main_page.get_first_popular_images_category()
    yandex_main_page.click_on(first_popular_images_category)
    time.sleep(3)
    images = yandex_main_page.get_image_bar()
    first_image = yandex_main_page.select_first_image(images)
    time.sleep(3)
    yandex_main_page.click_on(first_image)
    time.sleep(3)
    media_viewer = yandex_main_page.get_media_viewer()
    first_image_preview = yandex_main_page.get_image(media_viewer)
    first_image_src = first_image_preview.get_attribute('src')
    next_button = yandex_main_page.next_button(media_viewer)
    yandex_main_page.click_on(next_button)
    previous_button = yandex_main_page.previous_button(media_viewer)
    yandex_main_page.click_on(previous_button)
    current_image_preview = yandex_main_page.get_image(media_viewer)
    current_image_src = current_image_preview.get_attribute('src')
    assert first_image_src == current_image_src