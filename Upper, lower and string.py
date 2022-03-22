
# строчные буквы меняет на заглавные и наоборот

def swap_case(s):
    s_2 = ""

    for elem in s:
        if elem.isupper():
            s_2 += elem.lower()
        elif elem.islower():
            s_2 += elem.upper()
        else:
            s_2 += elem
    return s_2

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)