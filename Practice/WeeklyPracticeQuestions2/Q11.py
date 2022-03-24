def funcC(n, m):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    elif n > 1:
        return (2 * m * funcC(n-1, m) - funcC(n-2, m))

def funcH(n, m):
    if n == 0:
        return 1
    elif n == 1:
        return 2 * m
    elif n > 1:
        return ((2 * m * funcH(n-1, m)) - (2 * (n-1) * funcH(n-2, m)))

def funcL(n, m):
    if n == 0:
        return 1
    elif n == 1:
        return m
    elif n > 1:
        return (((2*n-1)*funcL(n-1,m)) - ((n-1)*funcL(n-2, m))) / n

def my_program(n, m, typ):


    if typ == 'L':
        return funcL(n,m)
    elif typ == 'C':
        return funcC(n,m)
    elif typ == 'H':
        return funcH(n,m)

print(my_program(2, 0, 'L'))
print(my_program(2, 1, 'C'))
