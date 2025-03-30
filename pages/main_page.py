from .base_page import BasePage
from .locators import MainPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
import allure

class MainPage(BasePage):
    @allure.step('Переходим в конструктор')
    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_LINK)

    @allure.step('Переходим в ленту заказов')
    def click_orders_feed(self):
        self.click_element(MainPageLocators.ORDERS_FEED_LINK)

    @allure.step('Переходим в личный кабинет')
    def click_personal_account(self):
        with allure.step('Закрываем модальное окно перед кликом'):
            self.close_modal_if_present()
        with allure.step('Кликаем по ссылке личного кабинета'):
            self.click_element(MainPageLocators.PERSONAL_ACCOUNT_LINK)

    @allure.step('Кликаем по ингредиенту')
    def click_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT)

    @allure.step('Перетаскиваем ингредиент в конструктор')
    def drag_ingredient(self):
        with allure.step('Находим исходный ингредиент'):
            source = self.find_element(MainPageLocators.INGREDIENT)
        with allure.step('Находим целевую область конструктора'):
            target = self.find_element(MainPageLocators.CONSTRUCTOR_DROP_TARGET)
        with allure.step('Выполняем перетаскивание через JavaScript'):
            self.drag_and_drop_js(source, target)
            time.sleep(1)

    @allure.step('Проверяем видимость деталей ингредиента')
    def is_ingredient_details_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_DETAILS)

    @allure.step('Получаем значение счетчика ингредиентов')
    def get_ingredient_counter(self):
        try:
            with allure.step('Находим и читаем значение счетчика'):
                counter = self.find_element(MainPageLocators.INGREDIENT_COUNTER, timeout=2)
                counter_text = counter.text.strip()
                return int(counter_text) if counter_text else 0
        except:
            return 0

    @allure.step('Кликаем по кнопке заказа')
    def click_order_button(self):
        with allure.step('Закрываем модальное окно перед кликом'):
            self.close_modal_if_present()
        with allure.step('Кликаем по кнопке'):
            self.click_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Проверяем видимость деталей заказа')
    def is_order_details_visible(self):
        return self.is_element_visible(MainPageLocators.ORDER_DETAILS_MODAL)

    @allure.step('Ожидаем идентификатор заказа')
    def wait_for_order_id(self):
        self.is_element_visible(MainPageLocators.ORDER_DETAILS_MODAL, timeout=10)
        return self.get_element_text(MainPageLocators.ORDER_ID)

    @allure.step('Проверяем, что мы на странице конструктора')
    def is_on_constructor_page(self):
        return self.driver.current_url == self.base_url
    