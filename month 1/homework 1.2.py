days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
expanses = [float(input(f"Введите расходы за {day}: ")) for day in days]

total = sum(expanses)
average = round(total / len(expanses), 1)

print("Общая сумма расходов за неделю: ", total)
print("Средний расход в день: ", average)

if average >= 1  and average <= 200:
    print('мало потрачено')
elif average >= 201 and average <= 500:
    print('средне потрачено')
elif average >= 501:
    print('много потрачено')
else:
    print('<')