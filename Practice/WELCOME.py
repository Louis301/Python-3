

#------------.|.------------
#---------.|..|..|.---------
#------.|..|..|..|..|.------
#---.|..|..|..|..|..|..|.---
#----------WELCOME----------
#---.|..|..|..|..|..|..|.---
#------.|..|..|..|..|.------
#---------.|..|..|.---------
#------------.|.------------


arr = input().split()
n = int(arr[0])
m = int(arr[1])
part = ".|."
w = "WELCOME"
s = ""

for i in range(n):
    if i < int(n / 2):
        for _ in range(i * 2 + 1):
            s += part
        print(s.center(m,'-'))
    elif i == int(n / 2):
        print(w.center(m,'-'))
    else:
        for _ in range(((n - 1) - i) * 2 + 1):
            s += part
        print(s.center(m,'-'))
    s = ""

