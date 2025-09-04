def guess_number():
    import sys

    low, hight = 1, 100
    attempts = []
    count = 0

    print("Загадайте число от 1 до 100, а я попробую угадать🤔")

    while True:
        if low > hight:
            print("Кажется, что-то пошло не так. Может, был нечестный ответ?")
            break

        guess = (low + hight) // 2
        attempts.append(guess)
        count += 1

        answer = input(f"Твое число {guess}? (ответь:'да', 'больше' или 'меньше'): ").strip().lower()

        if answer == "да":
            print(f"Я угадала число {guess}! Всего за {count} попыток.")

            with open("resalt.txt", "a") as f:
                f.write(f"Загаданное число: {guess}\n")
                f.write(f"Количество попыток: {count}\n")
                f.write(f"Список попыток: {attempts}\n")
                f.write(f"="*30 + "\n")

            break

        elif answer == "больше":
            low = guess +1
        elif answer == "меньше":
            hight = guess -1
        else:
            print("Неверный ввод. Пожалуйста, напишите: 'да', 'больше' или 'меньше'.")

if __name__ == "__main__":
   guess_number()