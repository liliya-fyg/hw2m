# data = ("O!", "0705","Megacom" , "0550", "Beeline",  "0770", "Katel", "0510", "Fonex", "0543")
# designations = data[0::2]
# codes = data[1::2]
#
# operator = {}
#
# operator = dict(zip(designations, [{c} for  c in codes]))
#
# for bad in ["Fonex", "Katel"]:
#     operator.pop(bad, None)
#
# operator["O!"].update({"0700", "0500"})
# operator["Megacom"].update({"0999", "0555"})
# operator["Beeline"].update({"0222", "0777"})
#
# for name, codes in operator.items():
#     print(f"{name} - {codes}")


#cod nomer 2

# data = ("O!", "0705","Megacom" , "0550", "Beeline",  "0770", "Katel", "0510", "Fonex", "0543")
#
# designation = []
# codes = []
#
# i = 0
# while i < len(data):
#     designation.append(data[i])
#     codes.append(data[i+1])
#     i += 2
#
# operators = {}
# j = 0
# while j < len(designation):
#     operators[designation[j]] = {codes[j]}
#     j += 1
#
# for bad in ["Fonex", "Katel"]:
#     operators.pop(bad, None)
#
# operators["O!"].update({"0700", "0500"})
# operators["Megacom"].update({"0999", "0555"})
# operators["Beeline"].update({"0222", "0777"})
#
# for name, codes in operators.items():
#     print(f"{name} - {codes}")


# cod nomer 3

# data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
#
# designation = []
# codes = []
#
# i = 0
# while i < len(data):
#     designation.append(data[i])     # название
#     codes.append(data[i+1])         # код
#     i += 2
#
# # собираем словарь
# operators = {}
# j = 0
# while j < len(designation):
#     operators[designation[j]] = {codes[j]}
#     j += 1
#
# # удаляем ненужных
# for bad in ["Fonex", "Katel"]:
#     operators.pop(bad, None)
#
# # обновляем коды
# operators["O!"].update({"0700", "0500"})
# operators["Megacom"].update({"0999", "0555"})
# operators["Beeline"].update({"0222", "0777"})
#
# # вывод
# for name, codes in operators.items():
#     print(f"{name} - {codes}")

# cod nomer 4


# data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
#
# designations = []
# codes = []
# i = 0
# while i < len(data):
#     item = data[i]
#     try:
#         int(item);
#         codes.appendet(item)
#     except ValueError:
#         designations.append(item)
#     # if item.isdigit():
#     #     codes.append(item)
#     # else:
#     #     designations.append(item)
#     # i += 1
#
# operators = {}
# j = 0
# while j < len(designations):
#     operators[designations[j]] = {codes[j]}
#     j += 1
#
# for bad in ("Fonex", "Katel"):
#     operators.pop(bad, None)
#
# operators["O!"].update({"0700", "0500"})
# operators["Megacom"].update({"0999", "0555"})
# operators["Beeline"].update({"0222", "0777"})
#
# for name, nums in operators.items():
#     print(f"{name} - {nums}")


# cod nomer 5


# data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
# designations = data[0::2]
# codes = data[1::2]
# i = 0
# while i < len(data):
#     item = data[i]
#
# operators = dict(zip(designations, [{c} for c in codes]))
#
# try:
#     int(item); codes.appendet(item)
# except ValueError:
#     designations.append(item)
#
# for bad in ("Fonex", "Katel"):
#     operators.pop(bad, None)
#
# operators["O!"].update({"0700", "0500"})
# operators["Megacom"].update({"0999", "0555"})
# operators["Beeline"].update({"0222", "0777"})
#
# for name, nums in operators.items():
#     print(f"{name} - {nums}")

# cod nomer 6


# data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
#
# designations = []
# codes = []
#
# i = 0
# while i < len(data):
#     designations.append(data[i])     # название
#     codes.append(data[i+1])          # код
#     i += 2
#
# # создаём словарь
# operators = {}
# j = 0
# while j < len(designations):
#     operators[designations[j]] = {codes[j]}
#     j += 1
#
# # удаляем ненужные
# for bad in ("Fonex", "Katel"):
#     operators.pop(bad, None)
#
# # обновляем коды
# operators["O!"].update({"0700", "0500"})
# operators["Megacom"].update({"0999", "0555"})
# operators["Beeline"].update({"0222", "0777"})
#
# # вывод
# for name, nums in operators.items():
#     print(f"{name} - {nums}")


# ==========================
# Задание 1. Ближайшее число
# ==========================

# def nearest_number(numbers, target):
#     # сортируем список по разнице (модуль разности)
#     sorted_numbers = sorted(numbers, key=lambda x: abs(x - target))
#     return (target, sorted_numbers)
#
#
# # ===========================================
# # Задание 2. Lambda + map и filter (примеры)
# # ===========================================
#
# def lambda_examples():
#     # map: умножаем каждое число на 2
#     numbers = [1, 2, 3, 4, 5]
#     doubled = list(map(lambda x: x * 2, numbers))
#     print("map (x2):", doubled)  # [2, 4, 6, 8, 10]
#
#     # filter: оставляем только чётные числа
#     evens = list(filter(lambda x: x % 2 == 0, numbers))
#     print("filter (чётные):", evens)  # [2, 4]
#
#
# # ==========================================================
# # Задание 3. Функция для вывода элемента по индексу (циклом)
# # ==========================================================
#
# def get_element(iterable=[1, 2, 3, 4, 5]):
#     while True:
#         index = input(f"Введите индекс элемента (или 'exit' для выхода): ")
#
#         if index.lower() == "exit":
#             print("Выход из программы.")
#             break
#
#         try:
#             index = int(index)  # пробуем превратить ввод в число
#             print(f"Элемент по индексу {index}: {iterable[index]}")
#         except ValueError:
#             print("Ошибка: индекс должен быть числом!")
#         except IndexError:
#             print(f"Ошибка: допустимые индексы от 0 до {len(iterable)-1}")


# =====================
# Главное меню программы
# =====================
#
# def main():
#     while True:
#         print("\nВыбери задание:")
#         print("1 - Ближайшее число")
#         print("2 - Примеры lambda (map, filter)")
#         print("3 - Вывод элемента по индексу")
#         print("0 - Выход")
#
#         choice = input("Введите номер: ")
#
#         if choice == "1":
#             print("\nЗадание 1:")
#             print(nearest_number([312, 996, 31, 1991], 1000))
#             print(nearest_number([5, 20, 18, 103, 4], 27))
#
#         elif choice == "2":
#             print("\nЗадание 2:")
#             lambda_examples()
#
#         elif choice == "3":
#             print("\nЗадание 3:")
#             get_element()
#
#         elif choice == "0":
#             print("Программа завершена.")
#             break
#         else:
#             print("Ошибка: выбери 0, 1, 2 или 3.")
#
# if __name__ == "__main__":
#     main()

# if name == "main":
#     main()

# def get_element(iterable=[1, 2, 3, 4, 5]):
#     while True:
#         index = input(f"Введите индекс элемента (или 'exit' для выхода): ")
#
#         if index.lower() == "exit":
#             print("Выход из программы.")
#             break
#
#         try:
#             index = int(index)  # пробуем превратить ввод в число
#             print(f"Элемент по индексу {index}: {iterable[index]}")
#         except ValueError:
#             print("Ошибка: индекс должен быть числом!")
#         except IndexError:
#             print(f"Ошибка: допустимые индексы от 0 до {len(iterable)-1}")
#

# 🔹 вызов функции
# get_elem

#
# geeks_founding_year = 2018
# current_year = int(input('enter current year: '))
# if (current_year - geeks_founding_year) > 5:
#     print('Образовательному центру больше 5 лет')
# else:
#     pass
# elif (current_year - geeks_founding_year) in range(1, 5 + 1):
#     print('Образовате
#     льному центру меньше 5 лет')

# for i in range(1, 10+1):
#     if i > 7:
#         print(i)
#     else:
#         print(False)

# kgz_regions = [
#     "Чуй", "Ыссык-куль", "Нарын", "Талас",
#     "Джалал-Абад", "Ош", "Баткен",
# ]
#
# first_tree = tuple(kgz_regions[:3])
# print(first_tree)

#
# geeks_in = ['Бишкек', 'Ош', 'Кара-Балта', 'Бишкек 9мкр']
#
# geeks_in.sort()
# geeks_in = [i.upper() for i in geeks_in]
# geeks_in = geeks_in[::-1]
# print(geeks_in)

geektech = {
       'name': 'Geektech',
       'address': 'Токтогула 175',
       'courses': {'Backend', 'Android'}
}

geeks = dict(name='GEEKS', address='И6раимова 103')
geektech.update(geeks)
geeks = geektech.copy()
geeks['courses'].update(['Frontend', 'iOS'])
print (geeks)