# Напишіть використовуючи бібліотеку range генератор паролів.
# Нехай у ньому буде на вибір користувача з чого скласти пароль
# (кирилиця, латиниця, цифри, великі та маленькі літери) також користувач обирає скільки символів він хоче
import random

print("Виберіть з яких символів буде складатися пароль:")
print("1 маленькі латинські  літери")
print("2 великі латинські  літери")
print("3 цифри")
print("4 кирилиця маленькі літери")
print("5 кирилиця велиці літери")
choice_user = input("Введіть свій вибір через пробіл: ")
choice = choice_user.split(' ')
length_pass = int(input("Скільки символів буде містити Ваш пароль: "))

complex_symbol = ''
if "1" in choice:
    complex_symbol += "abcdefghijklmnopqrstuvwxyz"
if "2" in choice:
    complex_symbol += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if "3" in choice:
    complex_symbol += "0123456789"
if "4" in choice:
    complex_symbol += 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
if "5" in choice:
    complex_symbol += 'АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'

password = ''.join([random.choice(complex_symbol) for i in range(length_pass)])
print(password)
