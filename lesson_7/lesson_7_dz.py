# ДЗ 7 Уроку
#
# Створіть два файли
# в 1-му напишіть такі функції:
# 1) сортування списка по зростанню числа, від меншого до більшого. Функція приймає список з чисел і повертає відсортований список.
# 2) сортування списка на спад, від більшого до меншого. Функція приймає список з чисел і повертає відсортований список.
# 3) сортування за кількістю букв у слові. Функція приймає список з слів і повертає відсортований список.
#
# 2-ий файл з трьома тестами який буде тестити ці три функції. В кожному тесті 1 тест.
# В тестових функціях ми ставимо типізацію. В першому файлі в всіх функціях проставляємо що приймає і що повертає.
# Встановіть собі пайтест і прораньте. До домашки отрім кода додайте скріншот прогона тестів.

list_growth = [100, 13, 79, 1, 25]
list_words = ["яблоко", "апельсин", "вікно", "мило", "гелікоптер"]


def sort_list_growth(list_growth:list) -> list:
    list_growth.sort()
    print(list_growth)
   # return list_growth





def sort_list_desc(list_growth:list) -> list:
    list_growth.sort(reverse = True)
    print(list_growth)
    return list_growth





def sort_list_words(list_words:list) -> list:
    list_words.sort(key=len)
    print(list_words)
    return list_words

# sort_list_growth([100, 13, 79, 1, 25])
# sort_list_desc([100, 13, 79, 1, 25])
# sort_list_words(["яблоко", "апельсин", "вікно", "мило", "гелікоптер"])

# sorted
# list_1 = [34, 456, 11, 12, -100, 77, 100, 35, 100.0, 100]
# list_2 = ['груша', 'грушаa', 'банан',  'яблуко', 'диня', "слива", "апельсин"]
# print(sorted(list_1, reverse=True))
# print(sorted(list_1, key=lambda x: x%2))
# print(sorted(list_2, key=len))
# print(sorted(list_2, key=lambda a: a[-1]))