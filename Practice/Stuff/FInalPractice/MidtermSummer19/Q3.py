while 1:
    n = int(input())
    if n == 0:
        break
    integerSet = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += integerSet[i]
    print(sum)
