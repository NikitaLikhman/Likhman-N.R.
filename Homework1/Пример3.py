import math
x = 3.74e-2
y = -0.825
z = 0.16e2
s = ((1 + math.sin(x + y)**2) / (x - (2*y) / (1 + x**2 * y**2))) * x**abs(y) + math.cos(math.atan(1/z))**2
print(f"s = {s:.6f}")