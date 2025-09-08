# layout_map = {
#     'й':'q', 'ц':'w', 'у':'e', 'к':'r', 'е':'t', 'н':'y', 'г':'u', 'ш':'i', 'щ':'o', 'з':'p', 'х':'[', 'ъ':']', 'ф':'a', 'ы':'s', 'в':'d', 'а':'f', 'п':'g',
#     'р':'h', 'о':'j', 'л':'k', 'д':'l', 'ж':';','э':"'", 'я':'z', 'ч':'x', 'с':'c', 'м':'v', 'и':'b', 'т':'n', 'ь':'m', 'б':',', 'ю':'.',
#
#     'q':'й', 'w':'ц', 'e':'у', 'r':'к', 't':'е', 'y':'н', 'u':'г', 'i':'ш', 'o':'щ', 'p':'з',
#     '[':'х', ']':'ъ', 'a':'ф', 's':'ы', 'd':'в', 'f':'а', 'g':'п', 'h':'р', 'j':'о', 'k':'л',
#     'l':'д', ';':'ж', "'":'э', 'z':'я', 'x':'ч', 'c':'с', 'v':'м', 'b':'и', 'n':'т', 'm':'ь',
#     ',':'б', '.':'ю'}
#
# def convert_word(word):
#     result = ''
#     for ch in word.lower():
#         if ch in layout_map:
#             result += layout_map[ch]
#         else:
#             result += ch
#     return result
#
# while True:
#     user_input = input("Введите слово (или 'exit' для выхода): ").strip()
#     if user_input.lower() == 'exit':
#         print("Выход из программы.")
#         break
#
#     converted = convert_word(user_input)
#     print("Обратная раскладка:", converted)


def вычисление_скидки(bal_dz, bal_test, visits):
    if 65 <= bal_dz <= 80 and 75 <= bal_test <= 100 and visits >= 6:
        return 3000
    elif 65 <= bal_dz <= 80 and 55 <= bal_test <= 74 and visits >= 8:
        return 2500
    elif 45 <= bal_dz <= 64 and 75 <= bal_test <= 100 and visits >= 6:
        return 2000
    elif 65 <= bal_dz <= 80 and 55 <= bal_test <= 74 and visits >= 6:
        return 2000
    elif 45 <= bal_dz <= 64 and 55 <= bal_test <= 74:
        return 1000
    else:
        return 0


bal_dz = int(input("Введите баллы за ДЗ: "))
bal_test = int(input("Введите баллы за тест: "))
visits = int(input("Введите количество посещений: "))

скидка = вычисление_скидки(bal_dz, bal_test, visits)
print("Сумма скидки:", скидка)
