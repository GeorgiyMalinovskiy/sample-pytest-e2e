import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


@allure.feature('Личный кабинет')
class TestProfile:
    @allure.title('Проверка перехода в личный кабинет для неавторизованного пользователя')
    def test_navigate_to_profile_unauthorized(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_personal_account()
        login_page = LoginPage(driver)
        assert login_page.is_on_login_page(), "Неавторизованный пользователь должен быть перенаправлен на страницу входа"

    @allure.title('Проверка перехода в личный кабинет для авторизованного пользователя')
    def test_navigate_to_profile_authorized(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_personal_account()
        profile_page = ProfilePage(driver)
        assert profile_page.is_on_profile_page(), "Авторизованный пользователь должен быть перенаправлен в личный кабинет"

    @allure.title('Проверка перехода в историю заказов')
    def test_navigate_to_orders_history(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_personal_account()
        profile_page = ProfilePage(driver)
        profile_page.click_orders_history()
        profile_page = ProfilePage(driver)
        assert profile_page.is_on_orders_history_page(), "Пользователь должен быть перенаправлен на страницу истории заказов"

    @allure.title('Проверка функционала выхода из аккаунта')
    def test_logout(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_personal_account()
        profile_page = ProfilePage(driver)
        profile_page.click_logout()
        login_page = LoginPage(driver)
        assert login_page.is_on_login_page(), "Пользователь должен быть перенаправлен на страницу входа"