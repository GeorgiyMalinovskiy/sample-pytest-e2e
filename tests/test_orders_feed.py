import pytest
import allure
import time

@allure.feature('Лента заказов')
class TestOrdersFeed:
    @pytest.fixture(autouse=True)
    def setup(self, pages):
        self.orders_feed = pages['orders_feed']
        self.login_page = pages['login_page']
        self.main_page = pages['main_page']

    @allure.title('Проверка модального окна с деталями заказа')
    def test_order_details(self, login):
        self.orders_feed.open()
        assert self.orders_feed.are_orders_visible(), "Заказы не отображаются в ленте"

        self.orders_feed.click_order()
        assert self.orders_feed.is_order_details_visible(), "Модальное окно с деталями заказа не отображается"

    @allure.title('Проверка отображения заказов в ленте')
    def test_orders_display(self, login):
        self.orders_feed.open()
        assert self.orders_feed.are_orders_visible(), "Заказы не отображаются в ленте"

    @allure.title('Проверка увеличения счетчика заказов')
    def test_orders_counter_increment(self, login):
        self.orders_feed.open()
        initial_total = self.orders_feed.get_total_orders_count()
        initial_today = self.orders_feed.get_today_orders_count()

        self.main_page.open()
        self.main_page.drag_ingredient()
        self.main_page.click_order_button()
        self.main_page.wait_for_order_id()

        self.orders_feed.open()
        assert self.orders_feed.get_total_orders_count() == initial_total + 1
        assert self.orders_feed.get_today_orders_count() == initial_today + 1

    @allure.title('Проверка появления заказа в разделе "В работе"')
    def test_order_in_progress(self, login):
        self.main_page.open()
        self.main_page.drag_ingredient()
        self.main_page.click_order_button()
        order_id = self.main_page.wait_for_order_id()

        self.orders_feed.open()
        time.sleep(5)

        assert self.orders_feed.is_order_in_progress(order_id), "Последний заказ не отображается в разделе 'В работе'"