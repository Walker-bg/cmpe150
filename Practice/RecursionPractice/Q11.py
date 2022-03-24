def indexOf(string, snipplet, x=0, y=0):
    if y+1 == len(snipplet):
        return x-y
    elif x+1 == len(string) and y+1 != len(snipplet):
        return -1

    if string[x] == snipplet[y]:
        return indexOf(string, snipplet, x+1, y+1)
    elif string[x] != snipplet[y]:
        return indexOf(string, snipplet, x+1, y=0) 
    
print(indexOf("Barack Obama", "Bar"))#0
print(indexOf("Barack Obama", "ck"))#4
print(indexOf("Barack Obama", "a"))#1
print(indexOf("Barack Obama", "McCain"))#-1
print(indexOf("Barack Obama", "BAR"))#-1