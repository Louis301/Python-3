#Progresses all triangles...
from math import pi, sqrt, pow, cos, acos

class Point:
    x = 0
    y = 0


point_A = Point()
point_A.x = float(input("Input coordinats of point A: \nx = "))
point_A.y = float(input("y = "))

point_B = Point()
point_B.x = float(input("Input coordinats of point B: \nx = "))
point_B.y = float(input("y = "))

point_C = Point()
point_C.x = float(input("Input coordinats of point C: \nx = "))
point_C.y = float(input("y = "))

a = sqrt(pow(point_C.x - point_B.x, 2) + pow(point_C.y - point_B.y, 2))
b = sqrt(pow(point_C.x - point_A.x, 2) + pow(point_C.y - point_A.y, 2))
c = sqrt(pow(point_B.x - point_A.x, 2) + pow(point_B.y - point_A.y, 2))

P = a + b + c
p = P / 2
s = sqrt(p * (p - a) * (p - b) * (p - c))
coaf = 180 / 3.14

alfa = acos((pow(c, 2) + pow(b, 2) - pow(a, 2)) / (2 * c * b)) * coaf
beta = acos((pow(c, 2) + pow(a, 2) - pow(b, 2)) / (2 * c * a)) * coaf
gamma = acos((pow(a, 2) + pow(b, 2) - pow(c, 2)) / (2 * a * b)) * coaf

print("\na = ", a)
print("b = ", b)
print("c = ", c)
print("P = ", P)
print("s = ", s)
print("alfa = ", alfa)
print("beta = ", beta)
print("gamma = ", gamma)
