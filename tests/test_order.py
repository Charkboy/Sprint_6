import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Urls, OrderData, Texts

class TestOrder:
    @pytest.mark.parametrize("order_data", OrderData.ALL_DATA)
    @pytest.mark.parametrize("button_locator", ["top", "bottom"])
    def test_order_scooter(self, driver, order_data, button_locator):
        driver.get(Urls.BASE_URL)
        main_page = MainPage(driver)
        main_page.close_cookie_banner()

        if button_locator == "top":
            main_page.click_order_top()
        else:
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