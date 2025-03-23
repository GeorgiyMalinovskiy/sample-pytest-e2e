from .base_page import BasePage
from .locators import ProfilePageLocators

class ProfilePage(BasePage):
    def click_orders_history(self):
        self.click_element(ProfilePageLocators.ORDERS_HISTORY_LINK)

    def click_logout(self):
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)

    def is_on_profile_page(self):
        return self.wait_for_url_contains('/profile') 