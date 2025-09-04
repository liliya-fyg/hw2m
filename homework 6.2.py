def nearest_number(numbers, target=0):
    return min(numbers, key=lambda x: abs(x - target))

print(nearest_number([1, 2, 3], 5))
print(nearest_number([-10, -5, 0, 2], 1))
print(nearest_number([4.5, 6.7, 9.1], 7))

