def power(m, n):
    return 1 if n == 0 else power(m, n-1) * m

print(power(0, 1))
print(power(2, 3))
print(power(1, 3))
print(power(2, 2))
print(power(2, 4))
print(power(3, 3))
print(power(2, 0))
