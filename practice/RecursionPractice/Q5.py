def GCD(a, b, x=2):
    if a==1 or b==1:
        return 1

    if a//x == a/x and b//x == b/x:
        return x*GCD(a/x, b/x, x)
    elif a//x != a/x and b//x == b/x:
        return GCD(a, b/x, x+1)       
    elif a//x == a/x and b//x != b/x:
        return GCD(a/x, b, x+1)
    elif a//x != a/x and b//x != b/x:
        return GCD(a, b, x+1)

print(GCD(2,2))
print(GCD(144,36))
print(GCD(81,7))
print(GCD(1,10))
print(GCD(5,15))