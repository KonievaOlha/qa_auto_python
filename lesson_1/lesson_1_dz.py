# Завдання №1
number1 = 16
number2 = 9
# Варіант №1
suma = number1 + number2
difference = number1 - number2
product = number1 * number2
fraction = number1 / number2
print(suma)
print(difference)
print(product)
print(fraction)

# Варіант №2
print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 / number2)

# Завдання №2
number_1 = int(input("Введіть перше число: "))
number_2 = int(input("Введіть друге число: "))
result_2 = number_1 % number_2
print(result_2)
#print(number_1 % number_2)

# Завдання №3
number_3 = int(input("Введіть перше число: "))
number_4 = int(input("Введіть друге число: "))
result_3 = number_3 // number_4
print(result_3)
#print(number_3 // number_4)

# Завдання №4
text_1 = int(input('Введіть рядок, який складається з цифр: '))
print("Тип даних введеного рядка:", type(text_1))
print("Введений рядок: ", text_1)

# Завдання №5
num_1 = input('введіть число 1: ')
num_2 = input('введіть число 2: ')
print("Конкатенація: ", num_1 + num_2)
print("Сума: ", int(num_1) + int(num_2))

# Завдання №6
name = input("Введіть Ваше ім'я: ")
birthday = int(input("Введіть Ваш рік народження: "))
year_now = int(input("Введіть, який зараз рік: "))
age = year_now - birthday
print("Ваше ім'я", name, "і Вам", age, "років")

# Завдання №7
c = float(input("Введіть градуси за Цельсієм: "))
# ? f = c * 9/5 + 32
f= float(c * 1.8000 + 32)
print('У фарінгейтах це стільки:', (float(f)))

# Завдання №8
F = float(input("Введіть градуси у фарінгейтах: "))
C = float((F - 32) / 1.8000)
print("у цельсіях це стільки", C)

# Завдання №9 с^2 = a^2 + b^2
side_a = int(input("Введіть довжину катета а = "))
side_b = int(input("Введіть довжину катета b = "))
side_c = ((side_a**2) ** (1/2))+ ((side_b**2) ** (1/2))
print("гіпотенуза с = ", side_c)

Завдання №10
n_child = int(input("Введіть кількість школярів: "))
k_apple = int(input("Введіть кількість яблук: "))
child = k_apple // n_child
basket = k_apple % n_child
print("Школяреві дістанеться яблук: ", child)
print("Яблук в кошику залишиться:", basket)

# Завдання №11
pencil = int(input("Введіть кількість куплених олівців, кількість яких не перевищує 109: "))
pen = int(input("Введеть кількість куплених ручок, кількість яких не перевищує 109: "))
marker = int(input("Введіть кількість куплених фломастерів, кількість яких не перевищує 109:  "))
price_one_pencil = 3
price_one_pen = price_one_pencil + 2
price_one_marker = price_one_pen + 7
# print(price_one_pencil)
# print(price_one_pen)
# print(price_one_marker)
all_price_pencil = pencil * price_one_pencil
all_price_pen = pen * price_one_pen
all_price_marker = marker * price_one_marker

price_all = all_price_pencil + all_price_pen + all_price_marker
print(price_all)

# Завдання №12
time = int(input("Введіть кількість хвилин пройшло з початку доби: "))
minute = time % 1440
hour = minute // 60
minute_1 = minute % 60
print("Електорнний годинник покаже годин:", hour)
print("і хвилин", minute_1)


# Завдання №13
s_all = int(input("Введіть загальну кількість зроблених журавликів: "))
serhii = s_all // 6
petro = serhii
katya = (serhii + petro) * 2
print("Катя зробила журавликів: ", katya)
print("Петро зробив журавликів: ", petro)
print("Сергій зробив журавликів: ", serhii)

# Завдання №14
zp = int(input("Введіть заробітну плату за 3 місяці: "))
vidsotok = int(input("Введіть відсоток, який ви маєте сплатити: "))
esv = 4422
zp3m = zp / 100 * vidsotok
podatok = zp - zp3m
print("Податок, який ви маєте сплатити:", podatok + esv)
