def isf(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Да")
    else:
        print("Нет")

isf(2024)
isf(1900)
isf(2000)