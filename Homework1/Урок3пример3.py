n = int(input())
h = n % 1440 // 60
minutes = n % 1440 % 60

print(h, minutes)
