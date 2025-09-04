import os
import datetime
import matplotlib.pyplot as plt

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


folder = "report"
if not os.path.exists(folder):
    os.mkdir(folder)

report_path = os.path.join(folder, "report.txt")
graph_path = os.path.join(folder, "expenses.png")

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



    budget = input("budget")
    with open(report_path, "w", encoding="utf-8") as file:
        file.write("🔹 ОТЧЁТ О РАСХОДАХ 🔹\n")
        file.write(f"Ученик: {name}\n")
        file.write(f"Дата и время: {date_str}\n\n")
        file.write("📊 Расходы в сомах:\n")
        file.write(f"Общая сумма: {total} сом\n")
        file.write(f"Средний расход: {average} сом/день\n")
        file.write(f"Бюджет: {budget} сом\n")

budget = safe_input("\nВведите ваш недельный бюджет в сомах: ")

if total > budget:
    budget_msg = f"⚠ Бюджет превышен на {round(total - budget, 1)} сом(ов)."
else:
    budget_msg = f"✅ Уложились в бюджет. Осталось {round(budget - total, 1)} сом(ов)."

    file.write("\n В валюте " + currency.upper() + ":\n")

    file.write(f"Общая сумма: {converted_total} {currency.upper()}\n")
    file.write(f"Средний расход: {converted_average} {currency.upper()}/день\n")
    file.write("\n📈 График расходов сохранён в файле expenses.png\n")


days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
expenses = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]

plt.figure(figsize=(8, 5))
plt.bar(days, expenses, color="skyblue", label="Расходы")

daily_budget = budget / 7
plt.axhline(y=daily_budget, color="red", linestyle="--", label="Средний дневной бюджет")

for i in range(len(expenses)):
    plt.text(i, expenses[i] + 20, f"{expenses[i]:.0f}", ha='center')



    plt.title("Расходы по дням недели")
plt.xlabel("Дни недели")
plt.ylabel("Сумма в сомах")
plt.legend()
plt.tight_layout()

plt.savefig(graph_path)
print(f" График сохранен как {graph_path}")

plt.close()



