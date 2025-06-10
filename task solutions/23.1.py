def f(cur, end):
    if cur == end:
        return True
    # избегаемые числа - 10 и 15
    if cur > end or cur == 10 or cur == 15:
        return False
    return f(cur + 1, end) + f(cur + 2, end) + f(cur + 3, end)

# обязательное число - 11
print(f(5, 11) * f(11, 18))

# Ответ: 176
