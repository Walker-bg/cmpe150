def recursiveSum(num):
    if num == 0:
        return 0
    return recursiveSum(num-1) + num

print(recursiveSum(0))
print(recursiveSum(1))
print(recursiveSum(2))
print(recursiveSum(3))
print(recursiveSum(4))
print(recursiveSum(5))
print(recursiveSum(500))