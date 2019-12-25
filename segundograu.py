
from math import sqrt

a = int(input("Digite o valor de a"))
b = int(input("Digite o valor de b"))
c = int(input("Digite o valor de c"))

delta = b**2 - 4*a*c
raizDelta = sqrt(delta)

x1 = (-b + raizDelta)/(2*a)
x2 = (-b - raizDelta)/(2*a)

print ("x1 = ", x1)
print ("x2 = ", x2)
