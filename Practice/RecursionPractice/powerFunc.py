def power(x, pow):
    if pow == 0:
        return 1
    return x*power(x, pow-1)

print(power(2, 5))
print(power(2, 1))
print(power(0, 4))
print(power(5, 0))
print(power(0, 0)) # :D 
print(power(1, 100))
print(power(11, 1))
