vowels = "а, о, у, ы, э, я, е, ю, и, a, e, i, o, u, y"
vowels += vowels.upper()
consonants = "б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ, b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, x, z"
consonants += consonants.upper()
while True:
    word = input("Введите слово (или 'stop' для выхода): ")

    if word.lower() == "stop":
        print("Программа завершена.")
        break

    total_letters = 0
    vowels_count = 0
    consonants_count = 0

    for letter in word:
            if letter in vowels:
                total_letters += 1
                vowels_count += 1
            elif letter in consonants:
                total_letters += 1
                consonants_count += 1

    if total_letters > 0:
        vowels_percent = round((vowels_count / total_letters) * 100, 2)
        consonants_precent = round((consonants_count / total_letters) * 100, 2)

        print(f"Всего букв: {total_letters}")
        print(f"Гласных: {vowels_count}")
        print(f"Согласных: {consonants_count}")
        print(f"Процент гласных: {vowels_percent}%")
        print(f"Процент согласных: {consonants_precent}%")
    else:
        print("В слове нет букв.")