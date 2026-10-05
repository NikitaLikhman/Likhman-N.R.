def scolor(x1, y1, x2, y2):
    if (x1 + y1) % 2 == (x2 + y2) % 2:
        print("Да")
    else:
        print("Нет")

scolor(1, 1, 2, 2)
scolor(1, 1, 1, 2)