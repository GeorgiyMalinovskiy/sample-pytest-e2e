from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import allure
import time
from .locators import BasePageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.nomoreparties.site/"
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Ждем закрытия модального окна, если оно присутствует')
    def close_modal_if_present(self):
        if self.is_element_visible(BasePageLocators.MODAL_OPENED, timeout=3):
            if self.is_element_visible(BasePageLocators.MODAL_CLOSE_BUTTON):
                with allure.step('Кликаем по кнопке закрытия модального окна'):
                    self.click_element(BasePageLocators.MODAL_CLOSE_BUTTON)
                    time.sleep(1)
            else:
                with allure.step('Ждем закрытия модального окна'):
                    EC.invisibility_of_element_located(BasePageLocators.MODAL_OPENED, timeout=10)

    @allure.step('Открываем страницу')
    def open(self):
        self.driver.get(self.base_url)
        self.wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')

    @allure.step('Ищем элемент')
    def find_element(self, locator, timeout=10):
        try:
            self.wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator),
                message=f"Не удалось найти элемент {locator}")
            return element
        except Exception as e:
            raise e

    @allure.step('Ищем элементы')
    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Не удалось найти элементы {locator}")

    @allure.step('Кликаем по элементу')
    def click_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент {locator} не кликабельный"
        )
        element.click()
    
    @allure.step('Вводим текст в поле {text}')
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Проверяем видимость элемента')
    def is_element_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step('Получаем текст элемента')
    def get_element_text(self, locator):
        element = self.find_element(locator)
        return element.text

    @allure.step('Ожидаем URL содержащий подстроку {text}')
    def wait_for_url_contains(self, text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.url_contains(text),
            message=f"URL не содержит подстроку {text}")

    @allure.step('Выполняем drag and drop с помощью JavaScript')
    def drag_and_drop_js(self, source_element, target_element):
        js_script = """
        function simulateDragDrop(sourceNode, destinationNode) {
            const EVENT_TYPES = {
                DRAGSTART: 'dragstart',
                DRAGENTER: 'dragenter',
                DRAGOVER: 'dragover',
                DROP: 'drop'
            };

            function createCustomEvent(type) {
                const event = new CustomEvent(type, {
                    'bubbles': true,
                    'cancelable': true
                });
                event.dataTransfer = {
                    data: {},
                    setData: function(type, val) {
                        this.data[type] = val;
                    },
                    getData: function(type) {
                        return this.data[type];
                    }
                };
                return event;
            }

            function dispatchEvent(node, type, event) {
                if (node.dispatchEvent) {
                    return node.dispatchEvent(event);
                }
                if (node.fireEvent) {
                    return node.fireEvent('on' + type, event);
                }
            }

            const dragStartEvent = createCustomEvent(EVENT_TYPES.DRAGSTART);
            dispatchEvent(sourceNode, EVENT_TYPES.DRAGSTART, dragStartEvent);

            const dropEvent = createCustomEvent(EVENT_TYPES.DROP);
            dispatchEvent(destinationNode, EVENT_TYPES.DROP, dropEvent);
        }
        simulateDragDrop(arguments[0], arguments[1]);
        """
        self.driver.execute_script(js_script, source_element, target_element)