def recursiveMultiplication(a, b):
    if b == 0:
        return 0
    return recursiveMultiplication(a, b-1) + a


print(recursiveMultiplication(5,6))
print(recursiveMultiplication(1,3))
print(recursiveMultiplication(0,0))
print(recursiveMultiplication(5,1))
print(recursiveMultiplication(5,0))
print(recursiveMultiplication(2,3))
