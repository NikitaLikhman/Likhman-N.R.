def min_of_three(x, y, z):
    m = x
    if y < m:
        m = y
    if z < m:
        m = z
    print(m)


min_of_three(5, 1, 0)