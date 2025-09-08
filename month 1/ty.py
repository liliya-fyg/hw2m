days = ["понедельник", "вторник", "среду", "четверг", "пятницу", "субботу", "воскресенье"]

expenses = []
for day in days:
    expense = float(input(f"Введите расходы за {day}: "))
    expenses.append(expense)

total = sum(expenses)
average = round(total / len(expenses), 1)

print("\nОбщая сумма расходов за неделю:", total)
print("Средний расход в день:", average)

if 1 <= average <= 200:
    print('мало потрачено')
elif 201 <= average <= 500:
    print('средне потрачено')
elif average >= 501:
    print('много потрачено')
else:
    print('<')