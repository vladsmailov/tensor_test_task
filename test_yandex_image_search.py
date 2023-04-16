def test_yandex_image_search_image_return(yandex_page):
    """
    Yandex search field image test.

    1) Checking menu button on the page "https://ya.ru/".
    2) Checking url-address for image-service page.
    3) Checking text in the searching field, while go to first
    page on the tab with popular image-categories.
    4) Checking result of the opening first image.
    5) Checking the switching before two results on
    the image preview page.
    Page -> Next Page
    Page Object != Next Page Object.
    6) Reversed checking of previous test:
    Page -> Next Page -> Previous page
    Page object == Previous page object.
    """
    # 1) First Test-case
    search_field = yandex_page.get_search_field()
    yandex_page.click_on(search_field)
    menu_button = yandex_page.get_menu_button()
    assert menu_button is not None
    # 2) Second Test-case
    yandex_page.click_on(menu_button)
    scrollbar = yandex_page.get_scrollbar()
    images_button = yandex_page.get_images_button(scrollbar)
    yandex_page.click_on(images_button)
    yandex_page.switch_windows(-1)
    url = yandex_page.get_url()
    assert url == 'https://yandex.ru/images/'
    # 3) Third Test-case
    first_popular_images_category = \
        yandex_page.get_first_popular_images_category()
    yandex_page.click_on(first_popular_images_category)
    images = yandex_page.get_image_bar()
    first_image = yandex_page.select_first_image(images)
    header = yandex_page.get_images_header()
    search_field = yandex_page.get_images_search_field(header)
    yandex_page.click_on(search_field)
    yandex_page.select_all_text()
    yandex_page.copy_all_text()
    text = yandex_page.get_copied_text()
    assert text is not None
    # 4) Fourth Test-case
    yandex_page.press_escape()
    yandex_page.click_on(first_image)
    media_viewer = yandex_page.get_media_viewer()
    image = yandex_page.get_image(media_viewer)
    assert image.get_attribute('class') == 'MMImage-Preview'
    # 5) Fifth Test-case
    first_image_preview = yandex_page.get_image(media_viewer)
    first_image_src = first_image_preview.get_attribute('src')
    next_button = yandex_page.next_button(media_viewer)
    yandex_page.click_on(next_button)
    second_image_preview = yandex_page.get_image(media_viewer)
    second_image_src = second_image_preview.get_attribute('src')
    assert first_image_src != second_image_src
    # 6) Sixth Test-case
    previous_button = yandex_page.previous_button(media_viewer)
    yandex_page.click_on(previous_button)
    current_image_preview = yandex_page.get_image(media_viewer)
    current_image_src = current_image_preview.get_attribute('src')
    assert first_image_src == current_image_src
