
# Выводит сообщения об ошибках, если какой-то операнд равен символу
# или делитель равен нулю

n = int(input())

for _ in range(n):

    try:
        a, b = input().split()
        c = int(a) // int(b)
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError:
        if a.isdigit():
            print("Error Code: invalid literal for int() with base 10: '" + b + "'")
        elif b.isdigit():
            print("Error Code: invalid literal for int() with base 10: '" + a + "'")
    else:
        print(c)