# Зробіть словник де буде табличка множення додавання ділення і віднімання чисел від 2 до 9(включно).
# Так як робили на уроці. Ці значення запишіть в словник з відповідними ключами "+", "-", "/", "*"
#
# Коли ви підготуєте це, запитайте в користувача яку табличку він хоче побачити
# (додавання, віднімання, множення, ділення). і виведіть йому цю табличку.


dict_table = {"*": [],
              "/": [],
              "+": [],
              "-": []}
input_sign = input("Введіть дію, таблицю якої хотіли б вивести на екран: ")
for numb_1 in range(2, 10):
    for numb_2 in range(2, 10):
        dict_table["*"].append(f"{numb_1}*{numb_2}={numb_1 * numb_2}")
        dict_table["/"].append(f"{numb_1}/{numb_2}={numb_1 / numb_2}")
        dict_table["+"].append(f"{numb_1}+{numb_2}={numb_1 + numb_2}")
        dict_table["-"].append(f"{numb_1}-{numb_2}={numb_1 - numb_2}")

if input_sign == "*":
    print(f"{dict_table.get('*')}")

elif input_sign == "/":
    print(dict_table.get("/"))
elif input_sign == "+":
    print(dict_table.get("+"))
elif input_sign == "-":
    print(dict_table.get("-"))
else:
    print(dict_table)
