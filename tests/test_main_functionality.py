import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.orders_feed_page import OrdersFeedPage

@allure.feature('Основной функционал')
class TestMainFunctionality:
    @allure.title('Проверка перехода в конструктор')
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_orders_feed()
        orders_feed_page = OrdersFeedPage(driver)
        assert orders_feed_page.is_on_orders_feed_page(), "Не удалось перейти в ленту заказов"
        main_page.click_constructor()
        assert main_page.is_on_constructor_page(), "Не удалось перейти в конструктор"

    @allure.title('Проверка перехода в ленту заказов')
    def test_navigate_to_orders_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_orders_feed()
        orders_feed_page = OrdersFeedPage(driver)
        assert orders_feed_page.is_on_orders_feed_page(), "Не удалось перейти в ленту заказов"

    @allure.title('Проверка модального окна с деталями ингредиента')
    def test_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient()
        assert main_page.is_ingredient_details_visible()

    @allure.title('Проверка закрытия модального окна ингредиента')
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient()
        main_page.close_modal_if_present()
        assert not main_page.is_ingredient_details_visible()

    @allure.title('Проверка счетчика ингредиентов')
    def test_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        initial_count = main_page.get_ingredient_counter()
        main_page.drag_ingredient()
        new_count = main_page.get_ingredient_counter()
        assert new_count == initial_count + 2

    @allure.title('Проверка создания заказа')
    def test_create_order(self, driver, login):
        main_page = MainPage(driver)
        main_page.open()
        main_page.drag_ingredient()
        main_page.click_order_button()
        assert main_page.is_order_details_visible(), "Модпльне окно заказа не отображается"