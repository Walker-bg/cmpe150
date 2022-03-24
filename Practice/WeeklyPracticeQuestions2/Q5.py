def ultraLucky(number, divisorSum=0, divisor = 2):
    digitList = list(str(number))
    if digitList.count('7') + digitList.count('4') == len(digitList):
        while number > 1:
            if number % divisor == 0:
                divisorSum += divisor
                number = number // divisor
                divisor = 2
            else:
                divisor+=1
        divisorSumList = list(str(divisorSum))
        if divisorSumList.count('7') + divisorSumList.count('4') == len(divisorSumList):
            return 1
        else:
            return 0
    else:
        return 0           


print(ultraLucky(4))
print(ultraLucky(410485630))
print(ultraLucky(2))
print(ultraLucky(1))
print(ultraLucky(7))
