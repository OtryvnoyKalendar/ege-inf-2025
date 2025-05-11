 # r - какой ход мы сделали в прошлый раз
def f(a, b, r):
    if a == b:
        return True
    if a > b:
        return False

    if a < b and r == '+1':
        return f(a + 2, b, '+2') + f(a * 2, b, '*2')
    if a < b and r != '+1':
        return f(a + 2, b, '+2') + f(a * 2, b, '*2') + f(a + 1, b, '+1')

print(f(1, 18, ''))

"""
478
"""
