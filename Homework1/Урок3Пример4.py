def calculate_lace_length(a, b, l, N):
    total_length = 2 * l + (2 * N - 1) * a + 2 * (N - 1) * b
    return total_length
print(calculate_lace_length(12, 14, 110, 13))
