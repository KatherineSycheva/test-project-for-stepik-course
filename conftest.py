import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """A handler that reads the language parameter from the command line."""
    parser.addoption('--lang', action='store', default="en",
                     help="Choose language: en, ru, fr, es etc.")


@pytest.fixture(scope="class")
def browser(request):
    language = request.config.getoption("lang")
    print("\nstart chrome browser for test..")
    options = webdriver.ChromeOptions()
    options.add_argument('--lang=' + language)
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

