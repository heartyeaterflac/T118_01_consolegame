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

def show_attempts(left):
    print("Осталось попыток:", left)



