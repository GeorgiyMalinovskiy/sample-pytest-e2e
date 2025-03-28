from .base_page import BasePage
from .locators import OrdersFeedLocators
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.by import By
import allure

class OrdersFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем страницу ленты заказов')
    def open(self):
        super().open()
        self.driver.get(f"{self.base_url}feed")

    @allure.step('Кликаем по заказу в ленте')
    def click_order(self):
        with allure.step('Ожидаем загрузку заказов'):
            self.wait.until(EC.presence_of_all_elements_located(OrdersFeedLocators.ORDER_CARD))
            orders = self.driver.find_elements(*OrdersFeedLocators.ORDER_CARD)
        
        if not orders:
            raise NoSuchElementException("No order cards found")
        
        with allure.step('Ожидаем кликабельности первого заказа'):
            first_order = orders[0]
            self.wait.until(EC.element_to_be_clickable(first_order))
        
        with allure.step('Кликаем по первому заказу'):
            first_order.click()
        
        with allure.step('Ожидаем появления модального окна'):
            self.wait.until(EC.presence_of_element_located(OrdersFeedLocators.ORDER_DETAILS_MODAL))
        
        return True

    @allure.step('Проверяем видимость деталей заказа')
    def is_order_details_visible(self):
        try:
            with allure.step('Ожидаем появления и видимости модального окна'):
                modal = self.find_element(OrdersFeedLocators.ORDER_DETAILS_MODAL)
                WebDriverWait(self.driver, 20).until(
                    EC.visibility_of(modal)
                )
            
            return True
        except TimeoutException as e:
            return False
        except Exception as e:
            return False

    @allure.step('Закрываем модальное окно')
    def close_modal(self):
        with allure.step('Ожидаем доступности кнопки закрытия'):
            self.wait.until(EC.presence_of_element_located(OrdersFeedLocators.CLOSE_MODAL_BUTTON))
            self.wait.until(EC.element_to_be_clickable(OrdersFeedLocators.CLOSE_MODAL_BUTTON))
        
        with allure.step('Кликаем по кнопке закрытия'):
            close_button = self.find_element(OrdersFeedLocators.CLOSE_MODAL_BUTTON)
            close_button.click()
        
        with allure.step('Ожидаем исчезновения модального окна'):
            self.wait.until(EC.invisibility_of_element_located(OrdersFeedLocators.ORDER_DETAILS))

    @allure.step('Получаем общее количество заказов')
    def get_total_orders_count(self):
        try:
            with allure.step('Находим счетчики заказов'):
                counters = self.find_elements(OrdersFeedLocators.ORDERS_COUNTER)
                if counters:
                    return int(counters[0].text)
            return 0
        except Exception as e:
            return 0

    @allure.step('Получаем количество заказов за сегодня')
    def get_today_orders_count(self):
        try:
            with allure.step('Находим счетчики заказов'):
                counters = self.find_elements(OrdersFeedLocators.ORDERS_COUNTER)
                if len(counters) > 1:
                    return int(counters[1].text)
            return 0
        except Exception as e:
            return 0

    @allure.step('Проверяем наличие заказа {order_number} в разделе "В работе"')
    def is_order_in_progress(self, order_number):
        with allure.step(f'Ищем заказ номер {order_number} в списке "В работе"'):
            orders = self.find_elements(OrdersFeedLocators.IN_PROGRESS_ORDERS)
            return order_number in ''.join([order.text for order in orders])

    @allure.step('Проверяем видимость заказов в ленте')
    def are_orders_visible(self):
        try:
            with allure.step('Ожидаем полной загрузки страницы'):
                self.wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')
            
            with allure.step('Проверяем наличие и видимость карточек заказов'):
                self.wait.until(EC.presence_of_element_located(OrdersFeedLocators.ORDER_CARD))
                self.wait.until(EC.visibility_of_element_located(OrdersFeedLocators.ORDER_CARD))
            
            with allure.step('Проверяем отображение всех заказов'):
                orders = self.find_elements(OrdersFeedLocators.ORDER_CARD)
                visible = len(orders) > 0 and all(order.is_displayed() for order in orders)
                return visible
        except TimeoutException as e:
            return False
        except Exception as e:
            return False 
        
    @allure.step('Проверяем, что мы на странице ленты заказов')
    def is_on_orders_feed_page(self):
        return self.wait_for_url_contains('feed')