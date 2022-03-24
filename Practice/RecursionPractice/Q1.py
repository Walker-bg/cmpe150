def isSubString(string1, string2):
    if len(string1) == 0:
        return True
    if len(string2) == 0:
        return False
    n=0
    if string1[n] != string2[n]:
        return isSubString(string1, string2[n+1:])
    elif string1[n] == string2[n]:
        return isSubString(string1[n+1:], string2[n+1:])


print(isSubString("AXY", "ADXCPY"))
print(isSubString("AXY", "YADXCP"))
print(isSubString("gksrek", "geeksforgeeks"))