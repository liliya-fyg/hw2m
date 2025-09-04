#Списки - List, кортежи - tuple. Индексы и среза.
#Встроенные функции к наборам эелементов.
#Списковое включение List comprehenshion.
# [object cycle condition]
# Объект цикл условие
# кортеж - открыт для использования, но закрыт для изменений. если писать в скобках (), то нужно добавить туда “，”

a = (23,)
a = list(a) # Это список
a = tuple(a) # Это кортеж
print(a)
print(type(a))


numbers = 2, 8, 5, 4, 1, 7, 9, 3, 6
print(numbers)
print(type(numbers))


"""Встроенные функции"""
#numbers = [2, 8, 5, 4, 1, 7, 9, 3, 6]
# print(min(numbers)) #минимальная цифра
# print(max(numbers))#максимальная цифра
# print(sum(numbers))#суммирует все цифры
# print(len(numbers))#сколько всего цифр



# student = ['Iskender', 'kanyshai', 'eldiyar', 'liliya']
# print(student)

"""delete"""
# student.remove('eldiyar')# Удаляет по названию объекта
# delete = student.pop(0)# Удаляет по номеру объекта (подлежит восстановлению)
# student.pop(0)# Удалаяет по номеру
# del student[-1]# Малая версия удаления
# student.clear()# Удаляет весь список
#
# print(student)
# print(delete)




"""edit"""
# student = [name.title() for name in student] # if 'r' in name, это условение ищет все объекты с определенным условием.
# print(student)
# student.sort(reverse=True) #Меняет в обратном порядке по алфавиту
# student.sort() # Меняет по алфавиту
#student.reverse() # В обратном порядке по списку
# student[0] = 'azamat' # Замена первоночальному объекту
#student.sort(key=len) # По количеству букв
#print(student)
# student2 = []
# for student in student2:
#     student2.append(student.title())
# print(student2)



"""add"""
# student.append('aizada') #Добавляет только 1 объект
# student.insert(0, 'jenishbek') #Добавляет определенное количесво
# student.extend(['mirlan', 'zhasmin']) #Можно довать более чем 1 объект
# student += (['mirlan', 'zhasmin']) #Работает так же как экстенд
# print(student)



"""Срезы [start:stop:step]"""
# print(student[:2])
# print(student[-2:])
# print(student[1:3])
# print(student[::])
# print(student[::2]) # Здесь выделяется каждый второй, потому что стоит 2 на конце. ее можно менять на другие числа. можно менять направление
# print(student[0][:2] + student[1][:2]) # Выделяется оределенное количество букв, тут на примере выделяется 4 буквы.
# print(student[-1][::-1]) #Пишется наоборот




"""Индексы"""
# print(student[0])
# print(student[2])
# print(student[-1])
# print(student[-2])
# print(student[0] [1])
#
#
# print(type(student))

 # while True:
 #  time = input('enter time: ').lower()
 #  if time == 'stop':
 #     break
 #  if time == 'morning' or time == 'утро':
 #     print('good morning')
 #  elif time == 'day' or time == 'день':
 #     print('good afternoon')
 #  elif time == 'evening' or time == 'вечер':
 #     print('good evening')
 #  else:
 #    print('hello')