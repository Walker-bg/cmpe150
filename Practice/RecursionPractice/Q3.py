def sumN(n):
    if n == 0:
        return 0
    return n + sumN(n-1)

print(sumN(0))
print(sumN(1))
print(sumN(2))
print(sumN(3))
print(sumN(4))
print(sumN(5))
