def funcH(num):
    if num <= 1:
        return num
    elif num%2==0:
        return funcH(num/2)
    elif num%2:
        return funcH((num-1)/2) + funcH((num+1)/2)

print(funcH(1))
print(funcH(5))
print(funcH(-10))
