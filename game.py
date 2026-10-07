# Начал с написания read_guess()
def read_guess():       # pапрашивает целое число от 1 до 50; повторяет вод до корректного ввода и возращает int
    while True:
        try:
            guess = int(input("Введите число от 1 до 50: "))

            if 1 <= guess <= 50:
                return guess

        except ValueError:
            print("Введите целое число")

# Возращает "больше" если 2 параметр больше 1го, "меньше" если меньше и "угадал" если равны
def compare_guess(guess, secret):
    if guess < secret:
        return "больше"
    elif guess > secret:
        return "меньше"
    else:
        return "угадал"

# Только выводит кол во попыток
def show_attempts(left):
    print("Осталось попыток:", left)

# Начальное состояние, обработка ходов, после окончания игры возвращение управления в меню. Код был позаимствован с прошлого группового проекта
def play_game():
    secret = 27
    attempts = 6

    while attempts > 0:
        show_attempts(attempts)

        guess = read_guess()
        result = compare_guess(guess, secret)

        print(result)

        if result == "угадал":
            print("Победа!")
            return

        attempts = attempts - 1

    print("Поражение. Вы не угадали число.")

# Выводит праивла игры для игрока
def show_rules():
    print("=== Правила игры ===")
    print("Загадано число от 1 до 50.")
    print("У вас есть 6 попыток.")
    print("После каждой ошибки игра подскажет:")
    print("- больше, если загаданное число больше вашего;")
    print("- меньше, если загаданное число меньше вашего.")
    print("Если вы угадаете число - победа.")
    print("Если потратите все 6 попыток не угадав - поражение.")

#
def read_choice(prompt, allowed):
    while True:
        choice = input(prompt)

        if choice == allowed[0]:
            return choice
        elif choice == allowed[1]:
            return choice
        elif choice == allowed[2]:
            return choice

        print("Некорректный выбор. Попробуйте ещё раз.")

def main():
    choice = ""

    while choice != "3":
        print("1. Начать игру")
        print("2. Правила")
        print("3. Выход")

        choice = input("Выберите: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            show_rules()
        elif choice == "3":
            print("До свидания!")

main()