monday = float(input("Введите расходы за понедельник: "))
tuesday = float(input("Введите расходы за вторник: "))
wednesday = float(input("Введите расходы за среду: "))
thursday = float(input("Введите расходы за четверг: "))
friday = float(input("Введите расходы за пятницу: "))
saturday = float(input("Введите расходы за субботу: "))
sunday = float(input("Введите расходы за восресенье: "))

total = monday + tuesday + wednesday + thursday + friday + saturday + sunday
average = round(total / 7, 1)

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