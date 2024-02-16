from random import randint

# 1) Напишіть ліст компрехеншин який формує список всіх чисел від 34 до 121 які діляться націло на 3 та на 2

list_comprehensions = [item for item in range(34, 121) if item % 3 == 0 and item % 2 == 0]
print(list_comprehensions)


# 2) Напишіть клас калькулятора де будуть 4 арифметичні дії плюс, мінус, додавання, множення - звичайні методи.
# і зробіть статік метод який буде виводити повідомлення, привіт я калькулятор.

class CalculatorClass:
    def add_numbers(self, num_1, num_2):
        self.result = num_1 + num_2
        return self.result

    def minus_numbers(self, num_1, num_2):
        self.result = num_1 - num_2
        return self.result

    def div_numbers(self, num_1, num_2):
        result = num_1 / num_2
        return result

    def mult_numbers(self, num_1, num_2):
        result = num_1 * num_2
        return result

    @staticmethod
    def st_method_print():
        print("Привіт, я калькулятор")


obj_1 = CalculatorClass()
print(obj_1.mult_numbers(2, 2))
print(obj_1.add_numbers(2, 2))
print(obj_1.div_numbers(2, 2))
print(obj_1.minus_numbers(2, 2))
CalculatorClass.st_method_print()

# Не оцінюється
# Напишіть ліст компрехеншн який буде заповнювати матрицю 7 на 7 клітинок рандомними цифрами, для рандому використовуйте
# random.randint (рандом в колесах пайтона)

list_comprehensions_1 = [[randint(1, 7) for j in range(7)] for i in range(7)]
print(list_comprehensions_1)
