from selene import have, be, browser


def test_search_1(setting_browser):
    browser.open("https://www.google.com/")
    browser.element('[name="q"]').type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_search_2():
    browser.open("https://www.google.com/")
    browser.element('[name="q"]').type('ыфа!2512афыа1йафывп!"№!"4').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    print("В поиске нет результатов...")
