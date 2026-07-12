import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Urls, OrderData, Texts

@allure.feature('Заказ самоката')
class TestOrder:

    # Тест с верхней кнопкой
    @allure.story('Заказ через верхнюю кнопку')
    @pytest.mark.parametrize("order_data", OrderData.ALL_DATA, ids=["data1", "data2"])
    def test_order_top_button(self, driver, order_data):
        allure.dynamic.title(f"Заказ через верхнюю кнопку с данными: {order_data['name']}")

        main_page = MainPage(driver)
        main_page.open(Urls.BASE_URL)
        main_page.close_cookie_banner()
        main_page.click_order_top()

        order_page = OrderPage(driver)
        order_page.wait_for_page_load()

        order_page.fill_name(order_data["name"])
        order_page.fill_surname(order_data["surname"])
        order_page.fill_address(order_data["address"])
        order_page.fill_metro(order_data["metro"])
        order_page.fill_phone(order_data["phone"])
        order_page.click_next()

        order_page.fill_date(order_data["date"])
        order_page.select_rental_period(order_data["rental_period"])
        order_page.select_color(order_data["color"])
        order_page.fill_comment(order_data["comment"])
        order_page.click_order_button()

        order_page.confirm_order()

        success_text = order_page.get_success_message()
        assert Texts.SUCCESS_MESSAGE_PART in success_text, "Сообщение об успехе не найдено"

    # Тест с нижней кнопкой
    @allure.story('Заказ через нижнюю кнопку')
    @pytest.mark.parametrize("order_data", OrderData.ALL_DATA, ids=["data1", "data2"])
    def test_order_bottom_button(self, driver, order_data):
        allure.dynamic.title(f"Заказ через нижнюю кнопку с данными: {order_data['name']}")

        main_page = MainPage(driver)
        main_page.open(Urls.BASE_URL)
        main_page.close_cookie_banner()
        main_page.click_order_bottom()

        order_page = OrderPage(driver)
        order_page.wait_for_page_load()

        order_page.fill_name(order_data["name"])
        order_page.fill_surname(order_data["surname"])
        order_page.fill_address(order_data["address"])
        order_page.fill_metro(order_data["metro"])
        order_page.fill_phone(order_data["phone"])
        order_page.click_next()

        order_page.fill_date(order_data["date"])
        order_page.select_rental_period(order_data["rental_period"])
        order_page.select_color(order_data["color"])
        order_page.fill_comment(order_data["comment"])
        order_page.click_order_button()

        order_page.confirm_order()

        success_text = order_page.get_success_message()
        assert Texts.SUCCESS_MESSAGE_PART in success_text, "Сообщение об успехе не найдено"