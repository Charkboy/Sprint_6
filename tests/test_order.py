import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import BASE_URL, ORDER_DATA
import time

class TestOrder:
    @pytest.mark.parametrize("order_data", ORDER_DATA)
    @pytest.mark.parametrize("button_locator", ["top", "bottom"])
    def test_order_scooter(self, driver, order_data, button_locator):
        driver.get(BASE_URL)
        print(f"\n➡️ Открыта главная страница: {driver.current_url}")
        main_page = MainPage(driver)
        main_page.close_cookie_banner()

        if button_locator == "top":
            print("🔼 Кликаем верхнюю кнопку 'Заказать'")
            main_page.click_order_top()
        else:
            print("🔽 Кликаем нижнюю кнопку 'Заказать'")
            main_page.click_order_bottom()

        # Проверяем, что URL изменился
        print(f"📍 Текущий URL после клика: {driver.current_url}")
        driver.save_screenshot(f"after_click_{button_locator}.png")

        # Явно ждём, что URL содержит /order
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        try:
            WebDriverWait(driver, 15).until(EC.url_contains("/order"))
            print("✅ URL содержит /order")
        except:
            print("❌ URL не содержит /order!")
            raise

        order_page = OrderPage(driver)
        order_page.wait_for_page_load()   # здесь падает
        # ...