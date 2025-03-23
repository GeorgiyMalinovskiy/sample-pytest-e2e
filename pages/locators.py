from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//button[@class='input__icon input__icon-action']")

class MainPageLocators:
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    ORDERS_FEED_LINK = (By.XPATH, "//p[text()='Лента Заказов']")
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")
    INGREDIENT = (By.CLASS_NAME, "ingredient-item")
    INGREDIENT_DETAILS = (By.CLASS_NAME, "ingredient-details")
    CLOSE_MODAL_BUTTON = (By.CLASS_NAME, "modal-close-button")
    INGREDIENT_COUNTER = (By.CLASS_NAME, "counter")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_DETAILS = (By.CLASS_NAME, "order-details")

class ProfilePageLocators:
    ORDERS_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

class OrdersFeedLocators:
    ORDER_CARD = (By.CLASS_NAME, "order-card")
    ORDER_DETAILS = (By.CLASS_NAME, "order-details")
    TOTAL_ORDERS_COUNTER = (By.CLASS_NAME, "orders-total")
    TODAY_ORDERS_COUNTER = (By.CLASS_NAME, "orders-today")
    IN_PROGRESS_ORDERS = (By.CLASS_NAME, "orders-in-progress")

class PasswordRecoveryLocators:
    EMAIL_INPUT = (By.NAME, "name")
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']") 