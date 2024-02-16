# 3) Напишіть тестовий клас який буде тестити попередній калькулятор тільки додавання і ділення.
#  до кожної математичної дії зробіть 5 тестів(використовуйте параметрайз, не пишіть руками зайвого).
#  Зробіть класову фікстуру(класметод) для сетапа і тердауна сетпа буде писати повідомлення в файл
#  коли ми запустили тест
#  та текстове повідомлення що ми стартанули. Тердаун буде писати повідомлення що ми закінчили і
#  також час коли закінчили
#  використайте вже відому вам бібліотеку дататайм

import pytest
from HW_lesson_15 import CalculatorClass
from datetime import datetime


class TestHwClass:
    @classmethod
    def setup_class(cls):
        cls.calc = CalculatorClass()
        start_time = datetime.now()
        with open("log.txt", "a") as file:
            file.write(f"\nStart Test {start_time}")
        print("Start test")

    @classmethod
    def teardown_class(cls):
        finish_time = datetime.now()
        with open("log.txt", "a") as file:
            file.write(f"\n Finish Test {finish_time}")
        print("\nFinish test")

    @pytest.mark.parametrize("num_1, num_2, result", [(2, 2, 4), (2, 3, 5), (1, 5, 6), (-1, 9, 8), (9, -2, 7)])
    def test_add_number(self, num_1, num_2, result):
        assert self.calc.add_numbers(num_1, num_2) == result

    @pytest.mark.parametrize("num_1, num_2, result", [(2, 2, 1), (2, 0, 0), (10, 2, 5), (15, 5, 3), (22, -2, -11)])
    def test_div_number(self, num_1, num_2, result):
        try:
            assert self.calc.div_numbers(num_1, num_2) == result
        except ZeroDivisionError:
            print(result)
