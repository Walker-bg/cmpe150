inpStr = input()
formInt = int(input())

if formInt == 0:
    inpList = list(inpStr)
    index = 0
    while index < len(inpList):
        if inpList[index] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            del inpList[index]
        else:
            index+=1
    print(''.join(inpList))

elif formInt == 1:
    inpStr = inpStr.upper()
    print(inpStr)
