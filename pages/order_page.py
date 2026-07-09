from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage(BasePage):
    def wait_for_page_load(self, timeout=15):
        self.close_cookie_banner()
        self.wait_for_element_present(OrderPageLocators.NAME_FIELD, timeout)

    def wait_for_second_page(self, timeout=10):
        self.close_cookie_banner()
        self.wait_for_element_present(OrderPageLocators.DATE_FIELD, timeout)

    def wait_for_modal(self, timeout=30):
        self.close_cookie_banner()
        self.wait_for_element_clickable(OrderPageLocators.CONFIRM_YES, timeout)

    def fill_name(self, name):
        self.send_keys_to_element(OrderPageLocators.NAME_FIELD, name, timeout=10)

    def fill_surname(self, surname):
        self.send_keys_to_element(OrderPageLocators.SURNAME_FIELD, surname, timeout=10)

    def fill_address(self, address):
        self.send_keys_to_element(OrderPageLocators.ADDRESS_FIELD, address, timeout=10)

    def fill_metro(self, metro_station):
        self.click_element(OrderPageLocators.METRO_FIELD, timeout=10)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(OrderPageLocators.METRO_DROPDOWN)
        )
        stations = self.driver.find_elements(*OrderPageLocators.METRO_DROPDOWN)
        for station in stations:
            if station.text.strip() == metro_station:
                station.click()
                return
        raise AssertionError(f"Станция метро '{metro_station}' не найдена")

    def fill_phone(self, phone):
        self.send_keys_to_element(OrderPageLocators.PHONE_FIELD, phone, timeout=10)

    def click_next(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON, timeout=10)
        self.wait_for_second_page()

    def fill_date(self, date):
        self.send_keys_to_element(OrderPageLocators.DATE_FIELD, date, timeout=10)
        self.driver.find_element(*OrderPageLocators.DATE_FIELD).send_keys(Keys.ESCAPE)

    def select_rental_period(self, period):
        self.close_cookie_banner()
        self.click_element(OrderPageLocators.RENTAL_PERIOD, timeout=10)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_any_elements_located(OrderPageLocators.RENTAL_OPTIONS)
        )
        options = self.driver.find_elements(*OrderPageLocators.RENTAL_OPTIONS)
        for opt in options:
            if opt.text.strip().lower() == period.lower():
                opt.click()
                return
        raise AssertionError(f"Вариант срока аренды '{period}' не найден")

    def select_color(self, color):
        if color.lower() == "чёрный":
            self.click_element(OrderPageLocators.COLOR_CHECKBOX_BLACK, timeout=5)
        elif color.lower() == "серая безысходность":
            self.click_element(OrderPageLocators.COLOR_CHECKBOX_GREY, timeout=5)

    def fill_comment(self, comment):
        self.send_keys_to_element(OrderPageLocators.COMMENT_FIELD, comment, timeout=10)

    def click_order_button(self):
        self.close_cookie_banner()
        self.js_click(OrderPageLocators.ORDER_BUTTON, timeout=10)
        self.close_cookie_banner()

    def confirm_order(self):
        self.wait_for_modal()
        self.js_click(OrderPageLocators.CONFIRM_YES, timeout=10)

    def get_success_message(self):
        self.close_cookie_banner()
        return self.get_text_from_element(OrderPageLocators.SUCCESS_MESSAGE, timeout=10)