def sum_of_digits(number, digitSum = 0):
    if number == 0:
        return digitSum
    digitSum += number%10
    return sum_of_digits(number//10, digitSum)

print(sum_of_digits(12423553))
print(sum_of_digits(3312))
print(sum_of_digits(0))
print(sum_of_digits(1))
print(sum_of_digits(12))