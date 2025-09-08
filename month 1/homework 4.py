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

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

reversed_letter = []
for i in range(len(letter) -1, -1,-1):
    reversed_letter.append(letter[i])
letter = reversed_letter

changed_letter = []
for ch in letter:
    if ch == 'C':
        changed_letter.append('c')
    elif ch == 'g':
        changed_letter.append('G')
    else:
        changed_letter.append(ch)
letter = changed_letter

squares = []
for numbers in numbers:
    squares.append(numbers ** 2)
numbers = squares

letter = tuple(letter)
numbers = tuple(numbers)

print("Кортеж letter:", letter)
print("Кортеж numbers:", numbers)
