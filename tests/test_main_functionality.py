import pytest
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage

@allure.feature('Основной функционал')
class TestMainFunctionality:
    @pytest.fixture
    def login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("test@example.com", "password123")
        return driver

    @allure.title('Проверка перехода в конструктор')
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_constructor()
        assert 'constructor' in driver.current_url

    @allure.title('Проверка перехода в ленту заказов')
    def test_navigate_to_orders_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_orders_feed()
        assert 'feed' in driver.current_url

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
        main_page.close_modal()
        assert not main_page.is_ingredient_details_visible()

    @allure.title('Проверка счетчика ингредиентов')
    def test_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        initial_count = main_page.get_ingredient_counter()
        main_page.click_ingredient()
        new_count = main_page.get_ingredient_counter()
        assert new_count == initial_count + 1

    @allure.title('Проверка создания заказа')
    def test_create_order(self, driver, login):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient()
        main_page.click_order_button()
        assert main_page.is_order_details_visible(), "Модпльне окно заказа не отображается" 