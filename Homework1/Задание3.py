name = input("Имя: ")
age = int(input("Возраст: "))
if not (0 < age < 75) or name.strip().capitalize() == "Иван":
    print("Ошибка возраста или имя Иван.")
elif age >= 16:
    print("Поздравляем вы поступили в ВГУИТ")
else:
    print(f"Сначала нужно окончить школу! Осталось учиться: {16 - age} лет.")