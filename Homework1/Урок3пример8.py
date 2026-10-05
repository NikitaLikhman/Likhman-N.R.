def match(a, b, c):
    if a == b == c:
        print(3)
    elif a == b or a == c or b == c:
        print(2)
    else:
        print(0)
        
match(5, 5, 5)
match(5, 5, 7)
match(5, 7, 9)