import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from data import BASE_URL

class TestLogo:
    def test_scooter_logo_redirects_to_main(self, driver):
        driver.get(BASE_URL)
        main_page = MainPage(driver)
        main_page.close_cookie_banner()
        # Переходим на страницу заказа, чтобы потом вернуться
        main_page.click_order_top()
        main_page.click_scooter_logo()
        # Проверяем, что URL стал базовым
        assert driver.current_url == BASE_URL, "Логотип Самоката не привел на главную"

    def test_yandex_logo_opens_dzen_in_new_tab(self, driver):
        driver.get(BASE_URL)
        main_page = MainPage(driver)
        main_page.close_cookie_banner()
        main_window = driver.current_window_handle

        main_page.click_yandex_logo()

        # Ждём появления второго окна
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[-1])

        # Ждём, пока в URL появится dzen или yandex
        WebDriverWait(driver, 10).until(
            lambda d: "dzen" in d.current_url.lower() or "yandex" in d.current_url.lower()
        )
        assert "dzen" in driver.current_url.lower() or "yandex" in driver.current_url.lower(), \
            "Логотип Яндекса не открыл Дзен"
        driver.close()
        driver.switch_to.window(main_window)