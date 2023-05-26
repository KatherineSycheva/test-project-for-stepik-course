import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def pytest_addoption(parser):
    """A handler that reads the language and browser parameter from the command line."""
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: en, ru, fr, es etc.")
    parser.addoption('--browser', action='store', default="chrome",
                     help="Choose browser: edge, firefox, chrome")



@pytest.fixture(scope="class")
def browser(request):
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser")
    print(f"\nstart browser {browser_name} for test..")
    if browser_name == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument('--lang=' + language)
        browser = webdriver.Edge(EdgeChromiumDriverManager().install(), options=options)
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.set_preference('intl.accept_languages', language)
        browser = webdriver.Firefox(GeckoDriverManager().install(),options=options)
    else:
        options = webdriver.ChromeOptions()
        options.add_argument('--language=' + language)
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

