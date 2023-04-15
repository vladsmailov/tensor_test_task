def test_yandex_text_search(yandex_page):
    """
    Yandex search field text test.

    1) Checking existing of searching field.
    2) Checking existing of suggestions in searching field.
    3) Checking that search give us result.
    4) Checking that first link in result list is required page.
    """
    search_field = yandex_page.get_search_field()    # 1) First Test-case
    assert search_field is not None
    yandex_page.enter_word(search_field, "Тензор")   # 2) Second Test-case
    suggestions = yandex_page.get_suggestions()
    assert suggestions is not None
    yandex_page.press_return_button(search_field)    # 3) Third Test-case
    results = yandex_page.get_page_source()
    assert results > 0
    first_link = yandex_page.get_first_link()        # 4) Fourth Test-case
    assert "https://tensor.ru/" in first_link
