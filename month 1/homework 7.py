#функция “ближайшее число”

def nearest_number(numbers, target):
    sorted_numbers = sorted(numbers, key=lambda x: abs(x - target))
    return  (target, sorted_numbers)

print(nearest_number([312, 996, 31, 1991], 1000))
print(nearest_number([5, 20, 18, 103, 4], 27))

# пример использования lambda функции с такими функциями как filter, map по одному примеру на своё усмотрение.

numbers = [1, 2, 3, 4 ,5]
doubled = list(map(lambda  x: x * 2, numbers))
print(doubled)

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda  x: x % 2 == 0, numbers))
print(evens)

#функция для вывода элемента списка/кортежа/строки (iterable) по указанному индексу.


def get_element(iterable = [1, 2, 3, 4, 5]):
    while True:
        index = input(f"Введите индекс элемента (или для 'exit' выхода): ")
        if index.lower() == "exit":
            break
        try:
            index = int(index)
            print(f"Элемент по индексу {index}:{iterable[index]}")
        except ValueError:
            print("Ошибка: индекс может быть только числом!")
        except IndexError:
            print(f"Ошибка: допустимые индексы от 0 до {len(iterable)-1}")

get_element()
