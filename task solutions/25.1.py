def f(n):
    lst = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            lst.append(i)
            lst.append(n // i)
    return sorted(set(lst))

for i in range(126849, 126872):
    # сколько делителей надо
    if len(f(i)) == 4:
        print(f(i)[2:])
