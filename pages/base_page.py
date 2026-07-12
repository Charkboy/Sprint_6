from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def close_current_window(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def find_elements(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
        return self.driver.find_elements(*locator)

    def click_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    def js_click(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    def send_keys_to_element(self, locator, text, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def get_text_from_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return element.text

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def close_current_window(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def wait_for_url_contains(self, part, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(part))

    def wait_for_url_to_be(self, url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))

    def wait_for_window_count(self, count, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(count))

    def wait_for_element_present(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_page_ready(self, timeout=60):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    def close_cookie_banner(self):
        try:
            cookie_button = (By.ID, "rcc-confirm-button")
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(cookie_button)).click()
        except TimeoutException:
            pass