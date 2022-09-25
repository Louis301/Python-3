print("input 10 numbers:")

i = 0
numbers = []

for i in range(3):
    numbers.append(float(input("number {0}: ".format(i + 1))))

numbers.sort()

print("Sorted: ", numbers)
