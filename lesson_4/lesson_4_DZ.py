# Задача 1
# Напишіть програму яка запитує в користувача вартість покупок, він їх вводе через пробіл, точна кількість не вказана.
# Вам потрібно до вартості покупок додати 6,5 відсотки податків.
# Потім питаєте чи є в користувача купон на знижку якщо є то питаєте це на суму чи на відсоток і
# потім віднімаєте суму або відсоток відповідно від ціни яку отримали раніше і пишете користувачу кінцеву суму.
# * завдання з зірочкою не впливає на бал. Округліть суму якщо копійок більше ніж 44 то це буде + 1 гривня, якщо менше.
# то тоді просто відкидаємо копійки від ціни.
## import math
# print(math.ceil(0.0001))
# print(math.floor(1.999))
# print(math.ceil(0.0001) == math.floor(1.999))

price_of_products = input("Введіть вартість покупок через пробіл: ")
price_of_prod = price_of_products.split()
new_number_list = []
print(price_of_prod)
for element in price_of_prod:
    new_number_list.append(int(element) + (int(element) / 100 * 6.5))
    print(new_number_list)
nnlist = []
coupon = input("Маєте купон на знижку? ")
if coupon == "так":
    type_coupon = bool(input("Якщо купон на суму, введіть 0, якщо на відсоток, то введіть 1: "))
    if type_coupon is True:
        for elem in new_number_list:
        nn_list.append(int(elem) - (int(elem) / 100 * 5))
        print(nnlist)
    else:
        # for element in price_of_prod:
        # new_number_list.append(int(element) + (int(element) / 100 * 6.5))
        # print(new_number_list)
else


# Задача 3
# Напишіть програму Банкомат. Втсановіть пін код для користувача(зробимо це константою).
# Запитайте в користувача Пін якщо він введе три рази не вірно то напишіть що карта заблокована.
# Використовуйте цикл while.
#

# PIN = 3399
#
# i = 0
# while i < 3:
#     user_pin = int(input("Введіть правильний PIN код: "))
#     i += 1
#     if user_pin != PIN:
#         if i == 3:
#             print("Невірний PIN код. Ваша карта заблокована")
#             break
#         print("Ви ввели неправильний PIN код. Спробуйте ще")
#
#     elif user_pin == PIN:
#         print("Вітаємо! ви ввели правильний PIN код")
#         break





# Задача 4
# Напишіть за допомогою f-string та format. Дві стрічки де буде підставлятись імя та вік з зміних
# name = "оЛенА"
# age = 21
# f_string = тут ваш код формата ф-стрінг. | повино вийти -> Я Олена, мені 21 рік
# format_string = тут ваш код формата формат стрінг | повино вийти -> Я Олена, мені 21 рік
# print(f_string)
# print(format_string)


# name = "оЛенА"
# age = 21
# f_fstring = (f"Я {name.title()}, мені {age} рік")
# format_string = """Я {0}, мені {1} рік""".format(name.title(), age)
# format_string_1 = """Я {name}, мені {age} рік""".format(name = name.title(), age = age)
# print(f_fstring)
# print(format_string)
# print(format_string_1)


# Задача 2
# Переробіть задачу з попереднього уроку враховуючи ваші знання з цього уроку, використайте цикл for in або while.

# list_of_products_write = input("Введіть через пробіл список покупок: ")
# list_of_products = list_of_products_write.split()
# print(list_of_products)
#
# i = 0
# while i < 5:
#     i+=1
#     del_element = int(input("Введіть порядковий номер елемента зі списку для видалення: "))
#     list_of_products.pop(del_element - 1)
#     print(list_of_products)
#
# if len(list_of_products) == 0:
#     print("Список пустий")
# else:
#     print("В списку лишилось ще ", list_of_products)
#
#
# add_product = input("Введіть через пробіл продукти, які бажаєте додати: ")
# add_prod_list = add_product.split()
# list_of_products.extend(add_prod_list)
# print(f"Ваш новий список: {list_of_products}! Гарного дня!")
