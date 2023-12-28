# # list_of_products_write = input("Введіть через пробіл список покупок: ")
# # list_of_products = list_of_products_write.split(" ")
# # print(list_of_products)
# # if len(list_of_products) != 0:
# #     pop
#
# # import copy
# # list_c = [23,45,656]
# # list_d = copy.deepcopy(list_c)
# # print(list_c)
# # print(list_d)
# # list_c.append(200)
# # print(list_c)
# # # print(list_d)
# # string_a = input()
# # list_of_number = string_a.split()
# # print(type(list_of_number), list_of_number)
# # print(list_of_number[1])
# list_i = [3,4,5]
# tuple_i = (3,4,5)
# for i in tuple_i:
#     print(i)
# tuple_2 = tuple(list_i)
# print(tuple_i, type(tuple_i))
# print(tuple_2, type(tuple_2))
# list_b = list_i
# list_b = list(tuple(list_i))  #
# print(id(list_i))
# print(id(tuple_2))
#
# new_string = "+".join("Привіт як в тебе справи")
# print(new_string)
# print(list_b)
# list_a = ["банани", "яблука", "шампунь"]
# string_from_list = " ".join(list_a)
# print(string_from_list)
#
#
# # extend - додавання списку в список (показати на стрічці різницю)
# list_a = [0,1]
# list_b = ["fdfs", "fds"]
# #list_a.append(list_b) # [0, 1, ['fdfs', 'fds']]
# list_a.extend(list_b) # [0, 1, 'fdfs', 'fds']
# print(list_a)
# print(list_b)
# list_12 = []
# list_22 = []
# list_12.append("привіт")  # ['привіт']
# list_22.extend("привіт")  # ['п', 'р', 'и', 'в', 'і', 'т']
# print(list_12)
# print(list_22)
# print(math.ceil(0.0001))
# print(math.floor(1.999))
import math
d = 60.31
c = 10.99 % 1
print(c)
if c > 0.44:
    print(math.ceil(c))
else:
    print(math.floor(c))