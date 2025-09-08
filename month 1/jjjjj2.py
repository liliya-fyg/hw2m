import datetime
import os
import matplotlib.pyplot as plt

#  Безопасный ввод числа (чтобы не ломалось)
def safe_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(" Введите корректное число.")


print("Введите расходы по дням недели:")
monday = safe_input("Понедельник: ")
tuesday = safe_input("Вторник: ")
wednesday = safe_input("Среда: ")
thursday = safe_input("Четверг: ")
friday = safe_input("Пятница: ")
saturday = safe_input("Суббота: ")
sunday = safe_input("Воскресенье: ")


total = monday + tuesday + wednesday + thursday + friday + saturday + sunday
average = round(total / 7, 1)


rates = {
    "сом": 1,
    "usd": 75,
    "eur": 90,
    "yuan": 12.5
}

#  Выбор валюты
print("\n В какую валюту перевести расходы?")
print("Доступные варианты: сом, usd, eur, yuan")

while True:
    currency = input("Введите валюту: ").lower()
    if currency in rates:
        break
    else:
        print("Такой валюты нет. Попробуйте ещё раз.")

converted_total = round(total * rates[currency], 1)
converted_average = round(average * rates[currency], 1)


if total == 'budget':
    budget_msg = f" Бюджет превышен на {round(total - 'budget', 1)} сом(ов)."
else:
    budget_msg = f" Уложились в бюджет. Осталось {round('budget' - total, 1)} сом(ов)."

print("\n Результаты:")
print(f"Общая сумма: {total} сом")
print(f"Средний расход: {average} сом/день")
print(budget_msg)
print(f"В валюте {currency.upper()}: {converted_total} {currency.upper()}, {converted_average} в день")

#  Имя + дата
name = input("\nВведите ваше имя для отчёта: ")
now = datetime.datetime.now()
date_str = now.strftime("%d.%m.%Y %H:%M")

#  Создание папки и путей
folder = "report"
if not os.path.exists(folder):
    os.mkdir(folder)

report_path = os.path.join(folder, "report.txt")
graph_path = os.path.join(folder, "expenses.png")

#  Сохраняем текстовый отчёт
with open(report_path, "w", encoding="utf-8") as file:
    file.write(" ОТЧЁТ О РАСХОДАХ \n")
    file.write(f"Ученик: {name}\n")
    file.write(f"Дата и время: {date_str}\n\n")

    file.write(" Расходы в сомах:\n")
    file.write(f"Общая сумма: {total} сом\n")
    file.write(f"Средний расход: {average} сом/день\n")
    file.write(f"Бюджет: {'budget'} сом\n")
    file.write(budget_msg + "\n")

    file.write("\n В валюте " + currency.upper() + ":\n")
    file.write(f"Общая сумма: {converted_total} {currency.upper()}\n")
    file.write(f"Средний расход: {converted_average} {currency.upper()}/день\n")

    file.write("\n График расходов сохранён в файле expenses.png\n")

print("\n Отчёт сохранён в:", report_path)

#  Построение графика с красной линией бюджета
days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
expenses = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]
daily_budget = 'budget' / 7

plt.figure(figsize=(8, 5))
plt.bar(days, expenses, color="skyblue", label="Расходы")
plt.axhline(y=daily_budget, color="red", linestyle="--", label="Средний дневной бюджет")

# Подписи
for i in range(len(expenses)):
    plt.text(i, expenses[i] + 20, f"{expenses[i]:.0f}", ha='center')

plt.title(" Расходы по дням недели")
plt.xlabel("Дни недели")
plt.ylabel("Сумма в сомах")
plt.legend()
plt.tight_layout()
plt.savefig(graph_path)
plt.close()

print(f" График сохранён в: {graph_path}")