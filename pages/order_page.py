from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
import time

class OrderPage(BasePage):
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_DROPDOWN = (By.XPATH, "//div[@class='select-search__select']/ul/li")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//div[@class='Dropdown-control']")
    RENTAL_OPTIONS = (By.XPATH, "//div[@class='Dropdown-menu']/div")
    COLOR_CHECKBOX_BLACK = (By.ID, "black")
    COLOR_CHECKBOX_GREY = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Buttons__1xGrp')]/button[text()='Заказать']")
    CONFIRM_YES = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class,'Order_ModalHeader__3FDaJ')]")

    def wait_for_page_load(self, retries=3):
        for attempt in range(retries):
            try:
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.NAME_FIELD))
                return
            except TimeoutException:
                print(f"⚠️ Попытка {attempt+1}: поле Имя не появилось, ждём ещё...")
                time.sleep(2)
        raise TimeoutException("Поле Имя не появилось после нескольких попыток")

    def wait_for_second_page(self):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.DATE_FIELD))

    def wait_for_success_modal(self):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))

    def fill_name(self, name):
        self.send_keys_to_element(self.NAME_FIELD, name)

    def fill_surname(self, surname):
        self.send_keys_to_element(self.SURNAME_FIELD, surname)

    def fill_address(self, address):
        self.send_keys_to_element(self.ADDRESS_FIELD, address)

    def fill_metro(self, metro_station):
        self.click_element(self.METRO_FIELD)
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.METRO_DROPDOWN))
        stations = self.driver.find_elements(*self.METRO_DROPDOWN)
        for station in stations:
            if station.text.strip() == metro_station:
                station.click()
                return
        raise AssertionError(f"Станция метро '{metro_station}' не найдена")

    def fill_phone(self, phone):
        self.send_keys_to_element(self.PHONE_FIELD, phone)

    def click_next(self):
        self.click_element(self.NEXT_BUTTON)
        self.wait_for_second_page()

    def fill_date(self, date):
        self.send_keys_to_element(self.DATE_FIELD, date)
        self.driver.find_element(*self.DATE_FIELD).send_keys(Keys.ESCAPE)
        time.sleep(0.5)

    def select_rental_period(self, period):
        self.force_click(self.RENTAL_PERIOD)
        options = self.driver.find_elements(*self.RENTAL_OPTIONS)
        for opt in options:
            if opt.text.strip() == period:
                opt.click()
                break

    def select_color(self, color):
        if color.lower() == "чёрный":
            self.click_element(self.COLOR_CHECKBOX_BLACK)
        elif color.lower() == "серая безысходность":
            self.click_element(self.COLOR_CHECKBOX_GREY)

    def fill_comment(self, comment):
        self.send_keys_to_element(self.COMMENT_FIELD, comment)

    def click_order_button(self):
        self.force_click(self.ORDER_BUTTON)

    def confirm_order(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.CONFIRM_YES)).click()

    def get_success_message(self):
        self.wait_for_success_modal()
        return self.find_element(self.SUCCESS_MESSAGE, timeout=15).text