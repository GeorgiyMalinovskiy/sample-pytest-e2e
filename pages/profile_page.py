from .base_page import BasePage
from .locators import ProfilePageLocators
import allure

class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликаем по ссылке "История заказов"')
    def click_orders_history(self):
        self.close_modal_if_present()
        self.click_element(ProfilePageLocators.ORDERS_HISTORY_LINK)

    @allure.step('Кликаем по кнопке "Выход"')
    def click_logout(self):
        self.close_modal_if_present()
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)
        self.wait_for_url_contains('/login')

    @allure.step('Проверяем, что мы на странице профиля')
    def is_on_profile_page(self):
        return self.wait_for_url_contains('profile')
    
    @allure.step('Проверяем, что мы на странице истории заказов')
    def is_on_orders_history_page(self):
        return self.wait_for_url_contains('order-history')