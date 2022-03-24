def funcG(num):
    if num <= 1:
        return 0
    elif num%2 == 0:
        return funcG(num/2) + (num/2)
    elif num%2:
        return funcG((num-1)/2) + ((num-1)/2)


print(funcG(3))
print(funcG(5))
print(funcG(-1))
print(funcG(0))
print(funcG(1))
print(funcG(10))