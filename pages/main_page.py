from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_LINK)

    def click_orders_feed(self):
        self.click_element(MainPageLocators.ORDERS_FEED_LINK)

    def click_personal_account(self):
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT_LINK)

    def click_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT)

    def is_ingredient_details_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_DETAILS)

    def close_modal(self):
        self.click_element(MainPageLocators.CLOSE_MODAL_BUTTON)

    def get_ingredient_counter(self):
        counter = self.find_element(MainPageLocators.INGREDIENT_COUNTER)
        return int(counter.text)

    def click_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)

    def is_order_details_visible(self):
        return self.is_element_visible(MainPageLocators.ORDER_DETAILS) 