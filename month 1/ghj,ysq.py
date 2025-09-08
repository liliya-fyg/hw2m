
def safe_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число, а не буквы. ")

rates = {"som": 1, "usd": 89, "yuan": 12.5, "eur": 96}

print("В какую валюту перевести расходы?")
print("Доступные варианты: som, usd, yuan, eur")

while True:
    currency = input("Введите валюту:").lower()
    if currency in rates:
        break
    else:
        print("Такой валюты нет. Попробуйте еще раз. ")

rate = rates[currency]
print("\n Введите расходы по дням недели:")
monday = float(input("Введите расходы за понедельник: "))
tuesday = float(input("Введите расходы за вторник: "))
wednesday = float(input("Введите расходы за среду: "))
thursday = float(input("Введите расходы за четверг: "))
friday = float(input("Введите расходы за пятницу: "))
saturday = float(input("Введите расходы за субботу: "))
sunday = float(input("Введите расходы за восресенье: "))



total = monday + tuesday + wednesday + thursday + friday + saturday + sunday
average = round(total / 7, 1)
converted_total = round(total / rate, 2)
converted_average = round(average / rate, 2)


print("\n Расходы за неделю: ")
print("Общая сумма:   ", total, "сом")
print("Средний расход:   ", average, "сом в день")

print("\n Итоги: ")
print(f"Общая сумма расходов: {total} som")
print(f"Средний расход в день: {average} som")

print(f"\n в {currency.upper()}: ")
print(f"Общая сумма: {converted_total} {currency.upper()}")
print(f"Средний расход: {converted_average} {currency.upper()} в день ")


import datetime
name = input("\nВведите ваше имя для отчета: ")

now = datetime.datetime.now()
date_str = now.strftime("%d. %m. %Y. %H:%M")

with open("report.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ О РАСХОДАХ\n")
    file.write(f"Ученик: {name}\n")
    file.write(f"Дата и время: {date_str}\n\n")

    file.write("расходы в сомах:\n")
    file.write(f"Общая сумма: {total} som\n")

    file.write("f В валюте {currency.upper()}:\n")
    file.write(f"Общая сумма: {converted_total} {currency.upper()}\n")
    file.write(f"Средний расход: {converted_average} {currency.upper()}\день\n")

    print("\n Отчет сохранен в файл report.txt")