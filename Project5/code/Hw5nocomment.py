import re
from decimal import Decimal
syntax_error = False #output file is generated at the end, syntax_error is here to keep track of errors
variableDict = {}
keywordDict = {"ve": 'and', "veya": 'or', "dogru": True, "yanlis": False, '(': '(', ')': ')', "kapa-parantez": ')', "ac-parantez": '(', '-': '-', '+': '+', '*': '*', "eksi": '-', "carpi": '*', "arti": '+', "sifir": 0, "bir": 1, "iki": 2, "uc": 3, "dort": 4, "bes": 5, "alti": 6, "yedi": 7, "sekiz": 8, "dokuz": 9,'0': 0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9}
textNumDict = {"sifir": 0, "bir": 1, "iki": 2, "uc": 3, "dort": 4, "bes": 5, "alti": 6, "yedi": 7, "sekiz": 8, "dokuz": 9}
numericalNumDict = {'0': 0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9}
logicalDict = {"ve": 'and', "veya": 'or', "dogru": True, "yanlis": False}
arithmeticDict = {'-': '-', '+': '+', '*': '*', "eksi": '-', "carpi": '*', "arti": '+', "sifir": 0, "bir": 1, "iki": 2, "uc": 3, "dort": 4, "bes": 5, "alti": 6, "yedi": 7, "sekiz": 8, "dokuz": 9,'0': 0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9}
def fileCleansing(line): #cleans up the line and returns a string without any whitespace or new line
    line = line.rstrip("\n").split()
    line = ' '.join(line)
    return line
def variableAndExpressionFinder(cleanLine): #finds the value or expression part of the line and returns it
    global syntax_error
    variableList = re.findall("^([a-zA-Z0-9]+) degeri .* olsun$", cleanLine)
    expressionList = re.findall("^[a-zA-Z0-9]+ degeri (.*) olsun$", cleanLine)
    if ((len(expressionList) == 1) and (len(variableList) == 1)  and (variableList[0] not in keywordDict) and (len(variableList[0]) < 11)):
        return [variableList[0], expressionList[0]] #returns a list of variable name expression part of the line
    else:
        syntax_error = True
        return [None, None]
def valueFinalizer(valueString):  #returns the appopriate parsed value if there is a syntax error in the value part, it finds it.
    global syntax_error             #for clean values only
    if valueString != None:
        if ('.' in valueString or re.search("nokta", valueString) or valueString in numericalNumDict or valueString in textNumDict):
            arithmeticOrLogical = "arr"
            if '.' in valueString:
                try:
                    parsedValue = float(valueString)
                except:
                    syntax_error = True
            elif re.search("nokta", valueString):
                numList = re.split(" nokta ", valueString)
                if len(numList) == 2:    
                    try:
                        parsedValue = int(textNumDict[numList[0]]) + int(textNumDict[numList[1]])*Decimal('0.1')
                    except:
                        syntax_error = True
            elif valueString in textNumDict:
                parsedValue = textNumDict[valueString]
            elif valueString in numericalNumDict:
                parsedValue = numericalNumDict[valueString]
        elif valueString in ["dogru", "yanlis"]:
            arithmeticOrLogical = "log"
            parsedValue = logicalDict[valueString]
        else:
            syntax_error = True
    if syntax_error == False:   
        return (parsedValue, arithmeticOrLogical)
    else:
        return None
# def expressionComputer(expressionString): #takes expressionFinder as input
#     global syntax_error
#     if expressionString == None:
#         pass
#     else:
#         expressionList = expressionString.split()
#         numOpenParan = 0
#         numCloseParan = 0
#         indx = 0
#         while indx < len(expressionList):
#             if syntax_error == False:
#                 tempExpr = expressionList[indx]
#                 if tempExpr == '(' or tempExpr == "ac-parantez":
#                     numOpenParan += 1
#                     expressionList[indx] = '('
#                 elif tempExpr == ')' or tempExpr == "kapa-parantez":
#                     numOpenParan += 1
#                     expressionList[indx] = ')'
#                 elif tempExpr == "nokta":
#                     expressionList[indx] = valueFinalizer(' '.join(expressionList[(indx-1):(indx+2)]))
#                     del expressionList[indx-1]
#                     del expressionList[indx+1]
#                     indx-=1
#                 elif '.' in tempExpr:
#                     expressionList[indx] = valueFinalizer(tempExpr)
#                 elif tempExpr in variableDict:
#                     expressionList[indx] = variableDict[tempExpr]
#                 elif tempExpr in keywordDict:
#                     pass
#             indx += 1
#         if numOpenParan != numCloseParan:
#             syntax_error = True
fileToRead = open("calc.in", 'r')
linesList = fileToRead.readlines()
tempIndex = 0
while tempIndex < len(linesList):
    cleanLine = fileCleansing(linesList[tempIndex])
    if cleanLine == '':
        del linesList[tempIndex]
    else:
        linesList[tempIndex] = cleanLine
        tempIndex+=1
if ("AnaDegiskenler" and "YeniDegiskenler" and "Sonuc") in linesList: #If every segment is here 
    anaIndex = linesList.index("AnaDegiskenler")  #we can start the loop, else just syntax error  
    yeniIndex = linesList.index("YeniDegiskenler") #Also I store the indices of these segments
    sonucIndex = linesList.index("Sonuc")
    for index in range(len(linesList)): #index and inputLine is reassinged for each loop
        inputLine = linesList[index]
        if syntax_error == True:
            break
        elif (index == anaIndex) or (index == sonucIndex) or (index == sonucIndex):
            continue
        elif index < yeniIndex: #while inside                                       ANADEGISKENLER
            variableAndExpressionList = variableAndExpressionFinder(inputLine)
            if variableAndExpressionList[0] not in variableDict:
                variableDict[variableAndExpressionList[0]] = valueFinalizer(variableAndExpressionList[1])
            else:
                syntax_error = True
        elif index < sonucIndex: #while inside YeniDegiskenler
            pass
        else: #while inside sonuc statement
            pass
    print(variableDict)
else:
    syntax_error = True
fileToRead.close()
############### OUTPUT PART ###############
fileToWrite = open("calc.out", 'w')
if syntax_error:
    fileToWrite.write("Dont Let Me Down")
else:
    fileToWrite.write("Here Comes the Sun")
fileToWrite.close()