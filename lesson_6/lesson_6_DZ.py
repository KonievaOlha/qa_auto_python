# Візьміть дві задачі з попередніх уроків, перша легка по вирішенню(декілька стрічок),
# друга більш складна і перепишіть їх на функції. Памятайте про Атамарність та god object.
# Там де написано що користувач має щось ввести то перероблюємо на функція приймає.
# Подивіться може можна за допомогою функції спростити код. В домашку вставте будь ласка опис задачі
# (далі(один з наступних уроків) буде домашка вашу домашку покрити тестами, але ми трохи поміняємо варіанти).

# Задача 1
# Уявимо що до нас прийшов наш друг або подруга і попросили написати додаток для покупок в магазині
# що б можна було скласти список продуктів та коли купуєш викреслювати(для викреслення питайте номер елемента,
# що б видалити по індексу треба його передати в pop list_a.pop(0) - видалить нульовий індекс, памятайте
# що користувач не знає що в нас індекси починаються з нуля)
# Також нам відомо що цей список має пять або більше елементів.
# Після кожного видалення елементу виводьте наш оновлений список.
# Після 5 видалень перевірте чи список пустий якщо не пустий напишіть що ось ще є продукти, якщо пусти то напишіть
# про це.
# Також після цього кроку запропонуйте користувачу написати ще продуктів та додати його в кошик. і виведіть їх на
# екран. Але цього разу вже без видалень.
# кроки:
# Спочатку пропонуємо користувачу ввести продукти.
# Робимо 5 запитів на видалення
# Перевіряємо корзину
# Пропонуємо додати продукти
# Виводмо список і прощаємось

# Варіант 1

list_of_products = ["lemon", "banana", "juice", "candy", "chocolate", "cherry"]


def del_element_of_list(del_element):
    list_of_products.pop(del_element - 1)
    print(list_of_products)


element = 0
while element < 5:
    element += 1
    del_element_of_list(del_element=1)

if len(list_of_products) == 0:
    print("Список пустий")
else:
    print("В списку лишилось ще ", list_of_products)

add_product = "tea"
add_prod_list = add_product.split()
list_of_products.extend(add_prod_list)
print(f"Ваш новий список: {list_of_products}! Гарного дня!")

# Варіант 2


list_of_products = ["lemon", "banana", "juice", "candy", "chocolate", "cherry"]


def del_element_of_list(del_element):
    list_of_products.pop(del_element - 1)
    print(list_of_products)


def len_list_of_product(list_of_products):
    if len(list_of_products) == 0:
        print("Список пустий")
    else:
        print("В списку лишилось ще ", list_of_products)
    return list_of_products


element = 0
while element < 5:
    element += 1
    del_element_of_list(del_element=1)
len_list_of_product(list_of_products)
add_product = "coffee"
add_prod_list = add_product.split()
list_of_products.extend(add_prod_list)
print(f"Ваш новий список: {list_of_products}! Гарного дня!")


# Задача 2
# Написати програму, яка зчитує два числа та виводить їхню суму, різницю, добуток та частку.
#
# Варіант 1


def sum1(number1: int, number2: int):
    suma = number1 + number2
    return suma


def difference(number1: int, number2: int):
    difference = number1 - number2
    return difference


def product(number1: int, number2: int):
    product = number1 * number2
    return product


def fraction(number1: int, number2: int):
    fraction = number1 / number2
    return fraction


print(sum1(2, 2))
print(difference(2, 2))
print(product(2, 2))
print(fraction(2, 2))


# Варіант 2
def calculator(sign):
    if sign == "+":
        suma = 3 + 2
        return suma
    elif sign == "-":
        difference = 6 - 2
        return difference
    elif sign == "*":
        product = 2 * 7
        return product
    elif sign == "/":
        fraction = 10 / 5
        return fraction


print(calculator(sign="+"))
print(calculator(sign="-"))
print(calculator(sign="*"))
print(calculator(sign="/"))


# Варіант 3
def calculator(sign, number_1, number_2):
    if sign == "+":
        suma = number_1 + number_2
        return suma
    elif sign == "-":
        difference = number_1 - number_2
        return difference
    elif sign == "*":
        product = number_1 * number_2
        return product
    elif sign == "/":
        fraction = number_1 / number_2
        return fraction


print(calculator(sign="+", number_1=6, number_2=3))
print(calculator(sign="-", number_1=6, number_2=3))
print(calculator(sign="*", number_1=6, number_2=3))
print(calculator(sign="/", number_1=6, number_2=3))

# Задача 3
# Напишіть програму яка запитує в користувача вартість покупок, він їх вводе через пробіл, точна кількість не вказана.
# Вам потрібно до вартості покупок додати 6,5 відсотки податків.
# Потім питаєте чи є в користувача купон на знижку якщо є то питаєте це на суму чи на відсоток і
# потім віднімаєте суму або відсоток відповідно від ціни яку отримали раніше і пишете користувачу кінцеву суму.
# * завдання з зірочкою не впливає на бал. Округліть суму якщо копійок більше ніж 44 то це буде + 1 гривня, якщо менше.
# то тоді просто відкидаємо копійки від ціни.


import math

price_of_products = ["23", "50", "11", "26", "100"]
new_price_of_products = []


def sum_coupon_remainder(sum_coupon: int | float):
    if sum_coupon % 1 > 0.44:
        print(f"Сума Ваших покупок = {math.ceil(sum_coupon)}")
    else:
        print(f"Сума Ваших покупок = {math.floor(sum_coupon)}")


def type_coupon_discount(type_coupon: str):
    if type_coupon == "1":
        sum_coupon = s_list - ((s_list * 5) / 100)
    else:
        sum_coupon = s_list - 10
    print(sum_coupon)
    return sum_coupon


for element in price_of_products:
    new_price_of_products.append(int(element) + ((int(element) * 6.5) / 100))
print(new_price_of_products)
s_list = sum(new_price_of_products)
print(s_list)
coupon = "так"
# coupon = "ні"
if coupon == "так":
    sum_coupon_remainder(type_coupon_discount(type_coupon="1"))
    sum_coupon_remainder(type_coupon_discount(type_coupon="0"))
else:
    print(f"Сума Ваших покупок = {s_list}! Гарного дня!")


# Задача 4
# Напишіть програму яка в користувача запитує два числа(можуть бути числа типу інт, а можуть бути в стр).
# Потім запитує це стр чи інт і в залежності від відповіді конкатенує їх або додає і
# повертає результат перемножений на три.


def data_type(number_1, number_2):
    result_1 = number_1 + number_2
    return result_1 * 3


print(data_type(number_1=str(1), number_2=str(0), ))
print(data_type(number_1=1, number_2=0, ))
