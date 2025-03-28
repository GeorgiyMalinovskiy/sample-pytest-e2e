import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from dotenv import load_dotenv
import os
from pages.orders_feed_page import OrdersFeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

# Load environment variables from .env file
load_dotenv()

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox',
                    help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser")
    driver = None
    
    try:
        if browser_name == "chrome":
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
        elif browser_name == "firefox":
            firefox_options = FirefoxOptions()
            driver = webdriver.Firefox(options=firefox_options)
        else:
            raise pytest.UsageError("--browser should be chrome or firefox")

        driver.maximize_window()
        yield driver
    except Exception as e:
        print(f"Failed to initialize {browser_name} driver: {str(e)}")
        raise
    finally:
        if driver:
            driver.quit()

@pytest.fixture
def test_email():
    return os.getenv('TEST_EMAIL')

@pytest.fixture
def test_password():
    return os.getenv('TEST_PASSWORD')

@pytest.fixture(scope="function")
def pages(driver):
    orders_feed = OrdersFeedPage(driver)
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    return {
        'orders_feed': orders_feed,
        'login_page': login_page,
        'main_page': main_page
    }

@pytest.fixture(scope="function")
def login(driver, pages, test_email, test_password):
    pages['login_page'].open()
    pages['login_page'].login(test_email, test_password)
    return driver 