# 1) додайте requirements.txt на ваш гіт
# 2) Виберіть будь-яку помилку яка вам подобається і зробіть функцію яка перевіряє на цю помилку(в функції try except)
# 3) зробіть функцію як ми робили з додаванням тільки замість двох чисел зробіть три числа і протестуйте її всіма
# трьома методами
# 4) перепишіть декоратор який заміряє час з уроку в домашку, можете його поклацати, як він працює
# Завдання 1
# https://github.com/KonievaOlha/qa_auto_python/blob/main/requirements
# Завдання 2
def audit_error(elem: int) -> int:
    try:
        print(elem / 2)
    except TypeError as e:
        print(f"element = {elem} {e}")


for element in [1, 2, "3", "4"]:
    audit_error(element)


def audit_error_2(num_1: int, num_2: int) -> (int, float):
    try:
        print(num_1 / int(num_2))
    except TypeError as t:
        print("Не вірний тип", t)
    except ZeroDivisionError as d:
        print("На нуль ділити не можна", d)
    except ValueError as v:
        print("Вказані символи не можна перетворити на число", v)


audit_error_2(4, 2)
audit_error_2("1", 1)
audit_error_2(3, 0)
audit_error_2(3, "Hello")


def audit_error_3(list_of_num: list) -> list:
    try:
        list_of_num.pop(0)
        print(list_of_num)
    except Exception as e:
        print(f"Видалення неможливе, {e}, список пустий")


audit_error_3([1, 2, 3])
audit_error_3(["5", 6, 79, "100"])
audit_error_3([])
audit_error_3(["one", "two", 3, 4, "five"])
audit_error_3([])
audit_error_3([7])


# Завдання 3


def add_numbers(num_1: int | float, num_2: int | float, num_3: int | float) -> int | float:
    add_result = num_1 + num_2 + num_3
    return add_result


# Завдання 4

from datetime import datetime
import time


def func_wrapper_time(func):
    def wrapper(*arg, **kwarg):
        start = datetime.now()
        result = func(*arg, **kwarg)
        delta_time = datetime.now() - start
        print("Час виконання функції ось такий: ", delta_time)
        return result

    return wrapper


@func_wrapper_time
def func_time_1(*arg, **kwarg):
    print("func_time_1")
    time.sleep(1)


@func_wrapper_time
def func_time_2(*args, **kwargs):
    print("func_time_2")
    time.sleep(2)


func_time_1()
func_time_2()
