string = input("Enter any string: ")

i = 0
for i in range(len(string)):
    if i % 2 == 0:
        print(string[i], end='')
