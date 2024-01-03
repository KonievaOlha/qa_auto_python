# ДЗ 7 Уроку
#
# Створіть два файли
# в 1-му напишіть такі функції:
# 1) сортування списка по зростанню числа, від меншого до більшого. Функція приймає список з чисел і повертає
# відсортований список.
# 2) сортування списка на спад, від більшого до меншого. Функція приймає список з чисел і повертає відсортований список.
# 3) сортування за кількістю букв у слові. Функція приймає список з слів і повертає відсортований список.
#
# 2-ий файл з трьома тестами який буде тестити ці три функції. В кожному тесті 1 тест.
# В тестових функціях ми ставимо типізацію. В першому файлі в всіх функціях проставляємо що приймає і що повертає.
# Встановіть собі пайтест і прораньте. До домашки отрім кода додайте скріншот прогона тестів.

list_growth = [100, 13, 79, 1, 25]
list_words = ["яблоко", "апельсин", "вікно", "мило", "гелікоптер"]
list_growth_for_assert = []


def sort_list_growth(list_growth_d: list) -> list:
    list_growth_d.sort()
    print(list_growth_d)
    return list_growth_d


def sort_list_desc(list_growth_d: list) -> list:
    list_growth_d.sort(reverse=True)
    print(list_growth_d)
    return list_growth_d


def sort_list_words(list_words_d: list) -> list:
    list_words_d.sort(key=len)
    print(list_words_d)
    return list_words_d


def sort_list_growth_for_assert(list_growth_for_assert_d: list) -> list:
    list_growth_for_assert_d.sort()
    print(list_growth_for_assert_d)
    return list_growth_for_assert_d


# sort_list_growth(list_growth)
# sort_list_desc(list_growth)
# sort_list_words(list_words)
# sort_list_growth_for_assert(list_growth_for_assert)
