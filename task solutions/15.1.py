# так
def f(A, x, y):
    return (x + 2*y < A) or (y > x) or (x > 60)

range_a = range(0, 200)
range_other = range(1, 100)
for A in range_a:
    table = (f(A, x, y) == True for x in range_other for y in range_other) # кортеж
    if all(table):
        print(A)
        break

# или через флаги
for A in range(0,200):
    b=True
    for x in range(0,100):
        for y in range(0,100):
            if ((x+2*y<A) or (y>x) or (x>60))==False:
                b=False
    if(b):
        print(A)
        break
