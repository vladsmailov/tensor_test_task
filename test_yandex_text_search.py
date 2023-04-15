from YandexPages import SearchHelper


def test_yandex_search_field_existing(browser):
    """Search field existing check."""
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    search_field = yandex_main_page.check_search_field()
    assert search_field is not None


def test_yandex_search_suggestions(browser):
    """Check suggestions."""
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    search_field = yandex_main_page.check_search_field()
    yandex_main_page.enter_word(search_field, "Тензор")
    suggestions = yandex_main_page.check_suggestions()
    assert suggestions is not None


def test_yandex_search_result(browser):
    """Checking that the results page is not empty."""
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    search_field = yandex_main_page.check_search_field()
    yandex_main_page.enter_word(search_field, "Тензор")
    yandex_main_page.press_return_button(search_field)
    results = yandex_main_page.get_page_source()
    assert results > 0


def test_first_link(browser):
    """Check first link."""
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    search_field = yandex_main_page.check_search_field()
    yandex_main_page.enter_word(search_field, "Тензор")
    yandex_main_page.press_return_button(search_field)
    first_link = yandex_main_page.check_first_link()
    assert "https://tensor.ru/" in first_link
