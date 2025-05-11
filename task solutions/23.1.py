def f(a, b):
    if a == b:
        return True
    # избегаемые числа - 10 и 15
    if a > b or a == 10 or a == 15:
        return False
    return f(a + 1, b) + f(a + 2, b) + f(a + 3, b)

# обязательное число - 11
print(f(5, 11) * f(11, 18))

"""
176
"""
