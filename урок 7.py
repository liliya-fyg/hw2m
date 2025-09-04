# lambda функции. Обработка исключений
# *args - arguments
#**kwargs - keyword arguments

try:
    print(2 + 'rt')
except:
    print('ошибка найдена')
else:
    print('ошибок не найдено')
finally:
    print('проверка завершена')

"""
от -30 до 15 - холодно
от 16 до 23 - тепло
от 24 до 40 - жарко
"""

while True:
    temperature = int(input('enter temperature: '))
    if temperature >= -30 and temperature <=15:
        print('холодно')
    elif temperature >=16 and temperature <=23:
        print('тепло')
    elif temperature >=24 and temperature <=40:
        print('жарко')
    else:
        print('несовместимо с жизнью температура!')
    data.append(temperature)




# student1 = ['kyrgyz', 'russian', 'english']
# student2 = ['turkish', 'chinese', 'english', 'kyrgyz']
#
# same_lang = list(set(student1) | set(student2))
# print(same_lang)
#
# diff_lang = list(set(student1) | set(student2))
# print(diff_lang)

# student1 = ['kyrgyz', 'russian', 'english']
# student2 = ['turkish', 'chinese', 'english', 'kyrgyz']
#
# same_lang = [lang for lang in student1 if lang not in student2]
#
# print(same_lang)
#
# student1 = ['kyrgyz', 'russian', 'english']
# student2 = ['turkish', 'chinese', 'english', 'kyrgyz']
#
# diff_lang = [lang for lang in student1 if lang not in student2] + [lang for lang in student2 if lang not in student1]
#
# print(diff_lang)


# student = ['iskender', 'mirlan', 'jasmin', 'ablai']
# print(student)

# map_student = list(map(lambda name: name.upper(), student))
# print(map_student)

# filter_student = list(filter(lambda name: 'a' in name, student)) #фильтрация данных.
# print(filter_student)

# sorted_students = sorted(student, key=lambda  name: name[1])
# print(sorted_students)

# lambda_func = lambda n1, n2,: n1 + n2
# print(lambda_func(2, 3))
# print(type(lambda_func))
#
# def def_func(n1, n2):
#     return n1 + n2
#
# print(def_func(2, 3))
# print(type(def_func))


# def up_first_letter(word: str):
#     return word.title()
#
#
# def show_words(func, words):
#     for word in words:
#         print(func(word))
#
# show_words(up_first_letter( ['tokmok', 'karakol', 'bishkek']))
# show_words(len, ['tokmok', 'karakol', 'bishkek'])


# def some_function(**kwargs):
#     return kwargs
# print()


# def plus(*args):
#     return sum(args)
# print(plus(1, 2, ))