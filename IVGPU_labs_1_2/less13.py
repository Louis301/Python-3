
import random

rand_num = random.randint(0, 10)
guessed_right = False

print("Загадано число от 0 до 10.\nУ вас есть три попытки отгадать его:")

for i in range(3):
    print("  Попытка {0}. ".format(i+1), end="")
    yours_num = int(input("Введите число: "))
    guessed_right = (yours_num == rand_num)
    if guessed_right:
        break

if guessed_right:
    print("\033[32m{0}\033[37m".format("Поздравляем! Вы угадали число"))
else:
    print("\033[31m{0} {1}\033[37m".format(
        "Не угадали... Правильное число:", rand_num))
