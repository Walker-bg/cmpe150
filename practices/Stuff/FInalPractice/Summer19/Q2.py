initialNum, maxTimes = map(int, input().split())

def collatz(num, time):
    if time == 0:
        return
    if num == 1:
        print(str(num))
        return
    elif num % 2: #even
        print(str(num), end=' ')
        return collatz(int((3*num)+1) ,time-1)
    else:
        print(str(num), end=' ')
        return collatz(int(num/2), time-1)

collatz(initialNum, maxTimes)