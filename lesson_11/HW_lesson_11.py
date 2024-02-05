# 1) Створіть клас Студент, в ньому обявіть дві змінні імя де збережети імя студента, та список його оцінок.
# створіть два метода в цьому класі, перший метод який буде вітатись
# і при вітання використовувати імя студента.
# другий метод буде виводити оцінки. Методи виводять результат через прінти.
#
# Створіть два екземпляра цього класу, в другому екземплярі змніть імя на своє(не міняючи нічого в класі). Вивідіть дві
# функції цих екземплярів, що б кожен студент привітався та сказав свої оцінки.
#
# 3) обновіть requirements.txt.txt
#
# ВСІ ЗАВДАННЯ ПОВИННІ БУТИ ПЕРЕВІРЕННІ flake8 за кожну помилку яку він знайде(окрім E501
# (там де кількість стрічок в ряд))
# буду знімати по 10 балів.

# Завдання 1
#
class StudentClass:
    stud_name = "Artem"
    stud_mark = [5, 5, 4, 4, 5, 3, 4, 5]

    def hello_student(self):
        self.hello = f"Привіт, мене звати {self.stud_name}"
        print(self.hello)

    def student_mark(self):
        self.mark = f"Я маю такі оцінки: {self.stud_mark}"
        print(self.mark)


obj_1 = StudentClass()
obj_1.hello_student()
obj_1.student_mark()
obj_2 = StudentClass()
obj_2.stud_name = "Olya"
# obj_2.stud_mark = [4, 5, 3, 4, 5, 3]
obj_2.hello_student()
obj_2.student_mark()

# чи можна виконати так?
# class StudentClass:
#     stud_name = "Artem"
#     stud_mark = [5, 5, 4, 4, 5, 3, 4, 5]
#
#     def hello_student(self):
#         self.hello_1 = f"Привіт, мене звати {self.stud_name}, я маю такі оцінки  {self.stud_mark}"
#         print(self.hello_1)
#
#
# obj_1 = StudentClass()
# obj_1.hello_student()
# obj_2 = StudentClass()
# obj_2.stud_name = "Olya"
# obj_2.stud_mark = [4, 5, 3, 4, 5, 3]
# obj_2.hello_student()
