data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
numbers = []
letter = []
for item in data_tuple:
    if type(item) == str:
        letter.append(item)
    else:
        numbers.append(item)

letter.append(True)
numbers = [n for  n in numbers if n != True]
numbers.remove(6.13)

new_nums = []
for n in numbers:
    new_nums.append(n)
    if n == 3:
        new_nums.append(2)
numbers = new_nums

numbers.sort()
letter = letter[::-1]

letter = [('G' if ch == 'g' else 'c' if ch == 'C' else ch) for ch in letter]

numbers = [n**2 for  n in numbers]

letter = tuple(letter)
numbers = tuple(numbers)

print("Кортеж letter:", letter)
print("Кортеж numbers:", numbers)
