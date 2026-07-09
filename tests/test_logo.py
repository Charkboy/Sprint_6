import pytest
from pages.main_page import MainPage
from data import Urls

class TestLogo:
    def test_scooter_logo_redirects_to_main(self, driver):
        driver.get(Urls.BASE_URL)
        main_page = MainPage(driver)
        main_page.close_cookie_banner()
        main_page.click_order_top()
        main_page.click_scooter_logo()
        main_page.wait_for_url_contains(Urls.BASE_URL, timeout=15)
        assert driver.current_url == Urls.BASE_URL, "Логотип Самоката не привел на главную"

    def test_yandex_logo_opens_dzen_in_new_tab(self, driver):
        driver.get(Urls.BASE_URL)
        main_page = MainPage(driver)
        main_page.close_cookie_banner()
        main_window = driver.current_window_handle

        main_page.click_yandex_logo()
        main_page.wait_for_number_of_windows(2, timeout=15)

        driver.switch_to.window(driver.window_handles[-1])
        main_page.wait_for_url_contains("dzen", timeout=15)  # или "yandex"
        assert "dzen" in driver.current_url.lower() or "yandex" in driver.current_url.lower(), \
            "Логотип Яндекса не открыл Дзен"
        driver.close()
        driver.switch_to.window(main_window)