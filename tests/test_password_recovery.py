import pytest
import allure
from pages.login_page import LoginPage

@allure.feature('Восстановление пароля')
class TestPasswordRecovery:
    
    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_navigate_to_recovery_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.click_forgot_password()
        assert 'forgot-password' in driver.current_url

    @allure.title('Проверка ввода email и кнопки восстановления')
    def test_email_input_and_recovery(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.click_forgot_password()
        login_page.enter_email("test@example.com")
        assert login_page.is_recover_button_enabled(), "Кнопка восстановления пароля недоступна после ввода email"

    @allure.title('Проверка переключения видимости пароля')
    def test_password_visibility(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.click_show_password()
        assert login_page.is_password_field_active() 