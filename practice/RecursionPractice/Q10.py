def isReverse(string1, string2):
    if len(string1)!=len(string2):
        return False
    if len(string1)<1:
        return True
    if string1[0].lower() == string2[-1].lower():
        return isReverse(string1[1:], string2[:-1])
    else:
        return False

print(isReverse("CSE143", "341esc"))#true
print(isReverse("Madam", "MaDAm"))#true
print(isReverse("Q", "Q"))#true
print(isReverse("", ""))#true
print(isReverse("e via n", "N aIv E"))#true
print(isReverse("Go! Go", "OG !OG"))#true
print(isReverse("Obama", "McCain"))#false
print(isReverse("banana", "nanaba"))#false
print(isReverse("hello!!", "olleh"))#false
print(isReverse("", "x"))#false
print(isReverse("madam I", "i m adam"))#false
print(isReverse("ok", "oko"))#false
