# prev - это предыдущий ход 
# def f(cur, end, prev):
def f(cur, prev):
    end = 18
    if cur == end:
        return True

    if cur > end:
        return False
    else:
        if prev == '+1':
            return f(cur + 2, '+2') + f(cur * 2, '*2')
        else:
            return f(cur + 2, '+2') + f(cur * 2, '*2') + f(cur + 1, '+1')

print(f(1, ''))
# Ответ: 478
