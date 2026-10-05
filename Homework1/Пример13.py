import math
x = 17.421
y = 10.365e-3
z = 0.828e5
s = (y + (x - 1)**(1/3))**(1/4) / (abs(x - y) * (math.sin(z)**2 + math.tan(z)))
print(f"s = {s:.6f}")