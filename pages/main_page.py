from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
import time

class MainPage(BasePage):
    # Верхняя кнопка (без класса UltraBig)
    ORDER_TOP_BUTTON = (By.XPATH, "//button[contains(@class,'Button_Button__ra12g') and not(contains(@class,'UltraBig'))]")
    ORDER_BOTTOM_BUTTON = (By.XPATH, "//button[contains(@class,'Button_UltraBig__UU3Lp')]")

    SCOOTER_LOGO = (By.XPATH, "//a[contains(@href,'/')]//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@href,'yandex')]//img[@alt='Yandex']")
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    @staticmethod
    def get_question_button(index):
        return (By.XPATH, f"(//div[@class='accordion__button'])[{index+1}]")

    @staticmethod
    def get_answer_panel(index):
        return (By.XPATH, f"(//div[@class='accordion__panel'])[{index+1}]")

    def wait_for_page_load(self):
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Заказать']"))
        )

    def close_cookie_banner(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.COOKIE_BUTTON)
            ).click()
        except TimeoutException:
            pass

    def click_order_top(self):
        self.wait_for_page_load()
        self.force_click(self.ORDER_TOP_BUTTON)
        WebDriverWait(self.driver, 15).until(EC.url_contains("/order"))

    def click_order_bottom(self):
        self.wait_for_page_load()
        self.close_cookie_banner()
        self.force_click(self.ORDER_BOTTOM_BUTTON)
        WebDriverWait(self.driver, 15).until(EC.url_contains("/order"))

    def click_question(self, index):
        self.close_cookie_banner()
        self.force_click(self.get_question_button(index))
        time.sleep(0.5)

    def get_answer_text(self, index):
        panel = self.find_element(self.get_answer_panel(index))
        return panel.text if panel else None

    def click_scooter_logo(self):
        self.force_click(self.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.force_click(self.YANDEX_LOGO)