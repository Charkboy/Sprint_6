from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    def click_order_top(self):
        self.close_cookie_banner()
        self.js_click(MainPageLocators.ORDER_TOP_BUTTON)

    def click_order_bottom(self):
        self.close_cookie_banner()
        self.js_click(MainPageLocators.ORDER_BOTTOM_BUTTON)

    def click_question(self, index):
        self.close_cookie_banner()
        self.js_click(MainPageLocators.get_question_button(index))

    def get_answer_text(self, index):
        return self.get_text_from_element(MainPageLocators.get_answer_panel(index))

    def click_scooter_logo(self):
        self.js_click(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.js_click(MainPageLocators.YANDEX_LOGO)