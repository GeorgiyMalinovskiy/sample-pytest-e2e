from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def enter_email(self, email):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    def click_forgot_password(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    def click_show_password(self):
        self.click_element(LoginPageLocators.SHOW_PASSWORD_BUTTON)

    def is_password_field_active(self):
        return self.is_element_visible(LoginPageLocators.PASSWORD_INPUT)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def is_recover_button_enabled(self):
        recover_button = self.find_element(LoginPageLocators.RECOVER_BUTTON)
        return recover_button.is_enabled() 