# Завдання 2
# 2) Напишіть 5 тестів з затримкою в 2 секунди кожен, один з тестів повинен мати унікальне імя.
#  Запустіть їх за домогою pytest-xdist ліби в 5 потоків.
#  Запустіть цей ваш унікальний тест з маркером -k
#  додайте скірншоти виконання(не забудьте додавати -v, що б я бачив що ви проганяли)
#  і біля скріншотів пропишіть команди
#  які ви використовували.


import time


def test_1():
    print("Test_1")
    time.sleep(2)


def test_2():
    print("Test_2")
    time.sleep(2)


def test_3():
    print("Test_3")
    time.sleep(2)


def test_4():
    print("Test_4")
    time.sleep(2)


def test_five():
    print("Test_five")
    time.sleep(2)
