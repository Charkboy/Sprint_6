import pytest
import allure
from pages.main_page import MainPage
from data import Urls

@allure.feature('Логотипы')
class TestLogo:

    @allure.story('Логотип Самоката')
    @allure.title('Переход на главную страницу при клике на логотип Самоката')
    def test_scooter_logo_redirects_to_main(self, driver):
        main_page = MainPage(driver)
        main_page.open(Urls.BASE_URL)
        main_page.close_cookie_banner()
        main_page.click_order_top()
        main_page.click_scooter_logo()
        main_page.wait_for_url_to_be(Urls.BASE_URL, timeout=15)
        assert main_page.get_current_url() == Urls.BASE_URL, "Логотип Самоката не привел на главную"

    @allure.story('Логотип Яндекса')
    @allure.title('Открытие Дзена в новой вкладке при клике на логотип Яндекса')
    def test_yandex_logo_opens_dzen_in_new_tab(self, driver):
        main_page = MainPage(driver)
        main_page.open(Urls.BASE_URL)
        main_page.close_cookie_banner()
        main_window = main_page.get_current_window_handle()

        main_page.click_yandex_logo()
        main_page.wait_for_window_count(2, timeout=15)

        main_page.switch_to_new_window()
        main_page.wait_for_url_contains("dzen", timeout=15)
        assert "dzen" in main_page.get_current_url().lower(), "Логотип Яндекса не открыл Дзен"

        main_page.close_current_window()