

fileName = input("Input a name of file (with extension): ")
procVariant = input("write/read?: ")

try:
    if procVariant == 'w':    
        with open(fileName, 'wt', encoding='utf-8') as file: # analog: file = open('text.txt', 'r', encoding='utf-8')
            while True:
                line = int(input("Input integer: "))
                file.write(str(line) + '\n')

    elif procVariant == 'r':
        with open(fileName, 'r', encoding='utf-8') as file:
            print(file.read())

except FileNotFoundError:
    print("Файл не найден")
except ValueError:
    print("Введено не число")

else:
    print("--- OK! ---")

finally:
    print("Поток закрыт")