import pytest
import allure
from pages.main_page import MainPage
from data import Urls

@allure.feature('Вопросы о важном')
class TestQuestions:

    @allure.story('Проверка ответов')
    @pytest.mark.parametrize("question_index", range(8))
    def test_question_answers(self, driver, question_index):
        driver.get(Urls.BASE_URL)
        main_page = MainPage(driver)
        main_page.close_cookie_banner()
        main_page.click_question(question_index)
        answer_text = main_page.get_answer_text(question_index)
        assert len(answer_text) > 0, f"Ответ на вопрос {question_index+1} пуст"