import pytest
import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage

@allure.feature('Личный кабинет')
class TestProfile:
    @pytest.fixture
    def login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("test@example.com", "password123")
        return driver

    @allure.title('Проверка перехода в личный кабинет')
    def test_navigate_to_profile(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_personal_account()
        profile_page = ProfilePage(driver)
        assert profile_page.is_on_profile_page()

    @allure.title('Проверка перехода в историю заказов')
    def test_navigate_to_orders_history(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_personal_account()
        profile_page = ProfilePage(driver)
        profile_page.click_orders_history()
        assert 'orders' in driver.current_url

    @allure.title('Проверка функционала выхода из аккаунта')
    def test_logout(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_personal_account()
        profile_page = ProfilePage(driver)
        profile_page.click_logout()
        assert 'login' in driver.current_url 