import random


def multyply(num1, num2):
    try:
        return float(num1) * float(num2)
    except ValueError:
        print("Параметр не является числом!")


try:
    user_num = float(input("Введите число больше пяти: "))
    rand_num = random.randint(0, 6)

    if user_num > 5:
        print("Случайное число:", rand_num)
        print("Результат:", multyply(rand_num, user_num))
    else:
        print("Число меньше или равно пяти! Некорректные данные")

except ValueError:
    print("Вы ввели не число!")
