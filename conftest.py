import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as OptionsF
from selenium.webdriver.chrome.options import Options as OptionsC


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en', help="Choose language")


# browser fixture (Chrome or Firefox can be chosen)
@pytest.fixture(scope='function')
def browser(request):
    # sending browser value
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')

    # conditions for browser and language
    if browser_name == "chrome":
        options = OptionsC()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = OptionsF()
        options.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("Choose chrome or firefox")

    # browser quiting
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

