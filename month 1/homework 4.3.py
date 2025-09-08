data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
numbers = []
letter = []

for item in data_tuple:
    if type(item) == str:
        letter.append(item)
    else:
        numbers.append(item)

numbers.remove(True)
letter.append(True)

final_numbers = []
for numbers in numbers:
    final_numbers.append(numbers)
    if numbers == 3:
        final_numbers.append(2)
numbers = final_numbers

numbers.remove(6.13)

numbers.sort()
letter = letter[::-1]

letter = [('G' if ch == 'g' else 'c' if ch == 'C' else ch) for ch in letter]

numbers = [numbers**2 for  numbers in numbers]
letter = tuple(letter)
numbers = tuple(numbers)

print("Кортеж letter:", letter)
print("Кортеж numbers:", numbers)
