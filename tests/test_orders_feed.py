import pytest
import allure
from pages.orders_feed_page import OrdersFeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

@allure.feature('Лента заказов')
class TestOrdersFeed:
    @pytest.fixture
    def login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("test@example.com", "password123")
        return driver

    @allure.title('Проверка отображения заказов в ленте')
    def test_orders_display(self, driver):
        orders_feed = OrdersFeedPage(driver)
        orders_feed.open()
        assert orders_feed.are_orders_visible()

    @allure.title('Проверка модального окна с деталями заказа')
    def test_order_details(self, driver):
        orders_feed = OrdersFeedPage(driver)
        orders_feed.open()
        orders_feed.click_order()
        assert orders_feed.is_order_details_visible()

    @allure.title('Проверка закрытия модального окна заказа')
    def test_close_order_modal(self, driver):
        orders_feed = OrdersFeedPage(driver)
        orders_feed.open()
        orders_feed.click_order()
        orders_feed.close_modal()
        assert not orders_feed.is_order_details_visible()

    @allure.title('Проверка статистики заказов')
    def test_orders_statistics(self, driver):
        orders_feed = OrdersFeedPage(driver)
        orders_feed.open()
        assert orders_feed.are_statistics_visible()

    @allure.title('Проверка увеличения счетчика заказов')
    def test_orders_counter_increment(self, driver, login):
        orders_feed = OrdersFeedPage(driver)
        orders_feed.open()
        initial_total = orders_feed.get_total_orders_count()
        initial_today = orders_feed.get_today_orders_count()

        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient()
        main_page.click_order_button()

        orders_feed.open()
        assert orders_feed.get_total_orders_count() == initial_total + 1
        assert orders_feed.get_today_orders_count() == initial_today + 1

    @allure.title('Проверка появления заказа в разделе "В работе"')
    def test_order_in_progress(self, driver, login):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient()
        main_page.click_order_button()
        
        orders_feed = OrdersFeedPage(driver)
        orders_feed.open()

        latest_order = orders_feed.get_total_orders_count()
        assert orders_feed.is_order_in_progress(latest_order), "Последний заказ не отображается в разделе 'В работе'"