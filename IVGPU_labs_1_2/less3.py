import random


def pswds_gen():
    passwords = []
    for i in range(5):
        pswd = []
        for j in range(8):
            pswd.append(random.randint(0, 9))
        passwords.append(''.join(map(str, pswd)))
    return passwords


passwords = pswds_gen()
print("Generating passwords... OK")

# print passwords
for el in passwords:
    print(el)

pswd = input("Enter the pswd: ")

pswd_found = False

for el in passwords:
    if pswd == el:
        pswd_found = True
        break

if pswd_found:
    print("Pswd was found! OK")
else:
    print("Not found...")
