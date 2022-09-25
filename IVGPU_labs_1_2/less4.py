
try:
    num = int(input("Enter any integer: "))
    i = 1
    while i <= num:
        print(i * i)
        i += 1

except ValueError:
    print("You didn't enter an integer")
