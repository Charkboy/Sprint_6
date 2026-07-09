from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Первая страница
    NAME_FIELD = (By.XPATH, "//input[contains(@class, 'Input_Input') and @placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_DROPDOWN = (By.XPATH, "//div[@class='select-search__select']/ul/li")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Далее']")

    # Вторая страница
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//div[@class='Dropdown-placeholder' and text()='* Срок аренды']")
    RENTAL_OPTIONS = (By.XPATH, "//div[@class='Dropdown-option']")
    COLOR_CHECKBOX_BLACK = (By.ID, "black")
    COLOR_CHECKBOX_GREY = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")

    # Модальное окно – кнопка "Да" по тексту
    CONFIRM_YES = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")