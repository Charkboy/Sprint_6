from selenium.webdriver.common.by import By

class MainPageLocators:
    # Верхняя кнопка "Заказать"
    ORDER_TOP_BUTTON = (By.XPATH, "//button[contains(@class,'Button_Button__ra12g') and not(contains(@class,'UltraBig'))]")
    # Нижняя кнопка "Заказать"
    ORDER_BOTTOM_BUTTON = (By.XPATH, "//button[contains(@class,'Button_UltraBig__UU3Lp')]")

    # Логотипы
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@href,'/')]//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@href,'yandex')]//img[@alt='Yandex']")

    # Куки-баннер
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    # Аккордеон вопросов
    @staticmethod
    def get_question_button(index):
        return (By.XPATH, f"(//div[@class='accordion__button'])[{index+1}]")

    @staticmethod
    def get_answer_panel(index):
        return (By.XPATH, f"(//div[@class='accordion__panel'])[{index+1}]")