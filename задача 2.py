import math
#Даны катеты прямоугольного треугольника a и b. Найдите его периметр P.
a = int(input())
b = int(input())
c = math.sqrt((a ** 2) + (b ** 2))
P = c + a + b
print('P =', P)
