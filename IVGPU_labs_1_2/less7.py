
def multyply(num1, num2):
    try:
        return float(num1) * float(num2)
    except ValueError:
        print("Arg is not number!")


print(multyply(input("input 1st number: "), input("input 2nd number: ")))
