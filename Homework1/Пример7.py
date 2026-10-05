import math
x = 0.1722
y = 6.33
z = 3.25e-4
term1 = 5 * math.atan(x)
term2 = (1/4) * math.acos(x) * (x + 3*abs(x - y) + x**2) / (abs(x - y)*z + x**2)
s = term1 - term2
print("term1 =", term1)
print("term2 =", term2)
print("s     =", s)