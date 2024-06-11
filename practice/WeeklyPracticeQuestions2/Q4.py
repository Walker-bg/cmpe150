def func(x):
    if x <= 0:
        return (x**2) - 2
    if x > 0:
        return (x**2) - x + 2

print(func(2))
print(func(0))
print(func(-1))
print(func(5))
print(func(-5))
