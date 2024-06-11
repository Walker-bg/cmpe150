def digitsMatch(int1, int2):
    if int1 == 0 and int2 == 0:
        return 0
        
    if int1%10 == int2%10:
        return 1+ digitsMatch(int1//10, int2//10)
    else:
        return digitsMatch(int1//10, int2//10)



print(digitsMatch(38, 34)) #1
print(digitsMatch(5, 5552)) #0
print(digitsMatch(892, 892)) #3
print(digitsMatch(298892, 7892)) #3
print(digitsMatch(380, 0)) #1
print(digitsMatch(123456, 654321)) #0
print(digitsMatch(1234567, 67)) #2
