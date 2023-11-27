# Задача 1

list_of_products_write = input("Введіть через пробіл список покупок: ")
list_of_products = list_of_products_write.split()
print(list_of_products)

del_element = int(input("Введіть порядковий номер елемента зі списку для видалення: "))
list_of_products.pop(del_element - 1)
print(list_of_products)

del_element = int(input("Введіть порядковий номер елемента зі списку для видалення: "))
list_of_products.pop(del_element - 1)
print(list_of_products)

del_element = int(input("Введіть порядковий номер елемента зі списку для видалення: "))
list_of_products.pop(del_element - 1)
print(list_of_products)

del_element = int(input("Введіть порядковий номер елемента зі списку для видалення: "))
list_of_products.pop(del_element - 1)
print(list_of_products)

del_element = int(input("Введіть порядковий номер елемента зі списку для видалення: "))
list_of_products.pop(del_element - 1)
print(list_of_products)

if len(list_of_products) == 0:
    print("Список пустий")
else:
    print("В списку лишилось ще ", list_of_products)

#якщо додавати декілька продуктів
add_product = input("Введіть через пробіл продукти, які бажаєте додати: ")
add_prod_list = add_product.split()
list_of_products = list_of_products + add_prod_list
print(f"Ваш новий список: {list_of_products}! Гарного дня!")


# #якщо додавати лише один продукт
# add_product = input("Введіть продукт, який бажаєте додати: ")
# list_of_products.append(add_product)
# print(f"Ваш новий список: {list_of_products}! Гарного дня!")