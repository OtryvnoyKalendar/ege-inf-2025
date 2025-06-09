def f(n):
    lst = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            lst.add(i)
            lst.add(n // i)
    return sorted(lst)

for i in range(126849, 126872):
    # сколько делителей надо
    if len(f(i)) == 4:
        print(f(i)[2:])
