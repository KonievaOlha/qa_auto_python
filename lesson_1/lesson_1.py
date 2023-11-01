 # komentar приклад псевдокоду : якщо буде змінна а більше 10 зроби це

 # для того щоб поставити курсор в декількох місцях затискаємо  альт
 # для коментуання декылькох ???
 # не писати змінні українською мовою
 змінна_1 = 20
 print(змінна_1)
 # не писати так(українські слова англійськими літерами)
 zmina_1 = 20
 print(zmina_1)

 # Правильний варіант
 variable = 20
 print(variable)
 print(type(variable))
 var = int(20)

 # todo питання на співбесіді Які типи данних є в пайтоні
 # INT
 variable_1 = 20
 variable_2 = 5
 variable_3 = 3

 # Створення дублікату ctrl+D

 print(variable_1 + variable_2) # без збереження в змінну
 print(variable_1 * variable_2) # без збереження в змінну

 result = variable_2 - variable_1 # більш вірний в написанні
 print(result)

 # Залишок від ділення %
 result_1 = variable_1 % variable_3
 print(result_1) # 2

 # Кількість ділення на ціло //
 result_2 = variable_1 // variable_3
 print(result_2) # 6


 # snake_case
 the_amount_of_students = 10
 variable_4 = 10

 # кирилиця з англійською в одній змінній дає помилку
 cup = 203
 print (cup)

 # починати змінну з цифри не вірно
 #2variable = 10
 #print(2variable)

 # "_" Єдиний спец символ який може бути присутній у змінній
 __student_name = ''

 # STR стрінг
 sample_text = "привіт, мене звати Оля"
 print(sample_text)
 print(type(sample_text))

 # Конкатинація " + "
 sample_text_1 = "999"
 sample_text_2 = "1"
 print(sample_text_1)
 print(type(sample_text_1))
 print(sample_text_1 + sample_text_2)


 # переобразованіє в інт |(трансформація типу данних)
 # sample_text_1_int = int(sample_text_1)
 # sample_text_2_int = int(sample_text_2)
 # result_5 = (sample_text_1_int + sample_text_2_int)
 # print(result_5)
age = int(input("скільки вам років?")) # default повертає str тип даних
print(age)
print(type(age))
