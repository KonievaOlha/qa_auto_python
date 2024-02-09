# Домашка
# Виберіть який з наступних магічних методів і реалізуйте його в простому класі:
# __ne__: To check if two objects are not equal.
# __lt__: To check if one object is less than another.
# __le__: To check if one object is less than or equal to another.
# __gt__: To check if one object is greater than another.
# __ge__: To check if one object is greater than or equal to another.
# Жодного з цих методів ми не розглядали на уроці, але вони працюють
# ідентично до метода ___eq__ який ми розглянули на уроці.
# Тобто вам треба буде змінити всього дві букви.
# І написати свою логіку яку ви хочте.
#
# Створіть два обьєта класа в якому ви це реалізували і зробіть перевірку що все працює


class MagicMethod:
    var_1 = None
    var_2 = None

    def __init__(self, var_1, var_2):
        self.a = var_1
        self.b = var_2
        self.var_ab = var_1 + var_2

    def __ne__(self, other):
        print(self.var_ab / other.var_ab)
        if not isinstance(other, type(self)):
            raise ZeroDivisionError
        elif self.var_ab / other.var_ab > 10:
            return True
        else:
            return False


# obj_1 = MagicMethod(0, 0)
obj_1 = MagicMethod(5, 10)
obj_2 = MagicMethod(3, 4)
print(obj_2 != obj_1)
