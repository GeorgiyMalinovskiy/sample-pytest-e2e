from selenium.webdriver.common.by import By

class BasePageLocators:
    MODAL_OPENED = (By.CSS_SELECTOR, "[class^='Modal_modal_opened']")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "[class^='Modal_modal_opened'] button[class^='Modal_modal__close']")

class LoginPageLocators:
    LOGIN_FORM = (By.CLASS_NAME, "Auth_login__3hAey")
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")

class MainPageLocators:
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    ORDERS_FEED_LINK = (By.XPATH, "//p[text()='Лента Заказов']")
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")
    INGREDIENT = (By.CSS_SELECTOR, "[class^='BurgerIngredient_ingredient']")
    INGREDIENT_DETAILS = (By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]//h2[text()='Детали ингредиента']")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "p[class^='counter_counter__num']")
    CONSTRUCTOR_DROP_TARGET = (By.CSS_SELECTOR, "section[class^='BurgerConstructor_basket']")
    ORDER_BUTTON = (By.CLASS_NAME, "button_button_size_large__G21Vg")
    ORDER_DETAILS_MODAL = (By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]//p[text()='идентификатор заказа']")
    ORDER_ID = (By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]//h2[not(text()='9999')]")

class ProfilePageLocators:
    ORDERS_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

class PasswordRecoveryLocators:
    EMAIL_INPUT = (By.NAME, "name")
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']") 

class OrdersFeedLocators:
    ORDER_CARD = (By.CSS_SELECTOR, "[class^='OrderHistory_link']")
    ORDER_DETAILS_MODAL = (By.CSS_SELECTOR, "[class^='Modal_modal_opened']")
    ORDERS_COUNTER = (By.XPATH, "//p[contains(@class, 'OrderFeed_number')]")
    IN_PROGRESS_ORDERS = (By.CSS_SELECTOR, "ul[class^='OrderFeed_orderListReady'] li")
