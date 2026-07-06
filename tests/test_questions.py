import pytest
from pages.main_page import MainPage
from data import BASE_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestQuestions:
    @pytest.mark.parametrize("question_index", range(8))
    def test_question_answers(self, driver, question_index):
        driver.get(BASE_URL)
        main_page = MainPage(driver)
        main_page.close_cookie_banner()

        # Ждём появления вопроса
        question_locator = main_page.get_question_button(question_index)
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(question_locator))

        main_page.click_question(question_index)

        # Проверяем, что ответ появился (не пустой)
        answer_text = main_page.get_answer_text(question_index)
        assert answer_text is not None and len(answer_text) > 0, f"Ответ на вопрос {question_index+1} пуст"