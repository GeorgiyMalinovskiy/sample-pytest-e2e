from .base_page import BasePage
from .locators import LoginPageLocators, PasswordRecoveryLocators
from selenium.webdriver.support import expected_conditions as EC
import allure

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем страницу логина')
    def open(self):
        super().open()
        with allure.step('Переходим в личный кабинет'):
            from .main_page import MainPage
            main_page = MainPage(self.driver)
            main_page.click_personal_account()
        with allure.step('Ожидаем появления формы логина'):
            self.wait.until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_FORM))

    @allure.step('Вводим email: {email}')
    def enter_email(self, email):
        with allure.step(f'Очищаем поле и вводим email: {email}'):
            email_input = self.find_element(LoginPageLocators.EMAIL_INPUT)
            email_input.clear()
            email_input.send_keys(email)
        with allure.step('Проверяем корректность введенного email'):
            actual_value = email_input.get_attribute('value')
            assert actual_value == email, f"Email input value mismatch. Expected: {email}, Got: {actual_value}"

    @allure.step('Вводим пароль')
    def enter_password(self, password):
        with allure.step('Очищаем поле и вводим пароль'):
            password_input = self.find_element(LoginPageLocators.PASSWORD_INPUT)
            password_input.clear()
            password_input.send_keys(password)
        with allure.step('Проверяем корректность введенного пароля'):
            actual_value = password_input.get_attribute('value')
            assert actual_value == password, f"Password input value mismatch. Expected: {password}, Got: {actual_value}"

    @allure.step('Нажимаем кнопку входа')
    def click_login_button(self):
        with allure.step('Находим и проверяем состояние кнопки'):
            login_button = self.find_element(LoginPageLocators.LOGIN_BUTTON)
        
        with allure.step('Кликаем по кнопке входа'):
            login_button.click()

        with allure.step('Ожидаем перехода на главную страницу'):
            self.wait.until(EC.url_to_be(self.base_url))

    @allure.step('Нажимаем "Забыли пароль?"')
    def click_forgot_password(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step('Нажимаем кнопку показа пароля')
    def click_show_password(self):
        self.click_element(LoginPageLocators.SHOW_PASSWORD_BUTTON)

    @allure.step('Проверяем активность поля пароля по типу')
    def is_password_field_active(self):
        password_field = self.find_element(LoginPageLocators.PASSWORD_INPUT)
        field_type = password_field.get_attribute('type')
        return field_type == 'text'

    @allure.step('Выполняем вход с email: {email}')
    def login(self, email, password):
        with allure.step(f'Вводим email: {email}'):
            self.enter_email(email)
        with allure.step('Вводим пароль'):
            self.enter_password(password)
        with allure.step('Нажимаем кнопку входа'):
            self.click_login_button()

    @allure.step('Проверяем доступность кнопки восстановления')
    def is_recover_button_enabled(self):
        recover_button = self.find_element(PasswordRecoveryLocators.RECOVER_BUTTON)
        enabled = recover_button.is_enabled()
        return enabled
    
    @allure.step('Проверяем, что мы на странице логина')
    def is_on_login_page(self):
        return self.wait_for_url_contains('/login')
    
    @allure.step('Проверяем, что мы на странице восстановления пароля')
    def is_on_recovery_page(self):
        return self.wait_for_url_contains('forgot-password')