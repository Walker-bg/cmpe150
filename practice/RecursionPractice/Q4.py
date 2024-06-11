def multiplyByPlus(a, b):
    if b == 0:
        return 0
    return a + multiplyByPlus(a, b-1)

print(multiplyByPlus(3, 5))
print(multiplyByPlus(3, 1))
print(multiplyByPlus(3, 0))
print(multiplyByPlus(3, 50))
