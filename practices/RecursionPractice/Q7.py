def x_ish(originalWord, isIn):
    if len(isIn) == 0:
        return True
    if isIn[0] in originalWord:
        return x_ish(originalWord, isIn[1:])
    else:
        return False

print(x_ish("original", "ginl"))
print(x_ish("original", "ginls"))