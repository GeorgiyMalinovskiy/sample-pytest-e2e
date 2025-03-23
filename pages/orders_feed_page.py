from .base_page import BasePage
from .locators import OrdersFeedLocators

class OrdersFeedPage(BasePage):
    def click_order(self):
        self.click_element(OrdersFeedLocators.ORDER_CARD)

    def is_order_details_visible(self):
        return self.is_element_visible(OrdersFeedLocators.ORDER_DETAILS)

    def get_total_orders_count(self):
        counter = self.find_element(OrdersFeedLocators.TOTAL_ORDERS_COUNTER)
        return int(counter.text)

    def get_today_orders_count(self):
        counter = self.find_element(OrdersFeedLocators.TODAY_ORDERS_COUNTER)
        return int(counter.text)

    def is_order_in_progress(self, order_number):
        orders = self.find_elements(OrdersFeedLocators.IN_PROGRESS_ORDERS)
        return any(order.text == str(order_number) for order in orders) 