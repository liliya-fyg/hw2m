#базовый синтакс, переменные, коментарии, встроенные функции
#типы данных: (базовые) строки, целые и дробные числа
#арифметические операторы
#str - string (строки)
#int - integer (целочисленное)
#float - floating (дробные)

name = input('what is your name? ').title()
surname = "o'nail"
age = int(input(f'{name},please,enter your age: '))
height = 1.78
current_year = 2025
born = current_year - age

print(f'name:{name} surname:{surname} born :{born} ')



