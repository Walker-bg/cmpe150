
s = input()


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

def sumOfDigits(s, summ):
    if len(s)<1:
        return summ
    if 47<ord(s[0:1])<58:
        return sumOfDigits(s[1:len(s)], summ+(ord(s[0:1])-48))
    else:
        return sumOfDigits(s[1:len(s)], summ)
        
print(sumOfDigits(s, 0))

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE


