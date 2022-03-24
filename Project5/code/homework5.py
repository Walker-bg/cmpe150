import re
from decimal import Decimal

############################## VARIABLES ##############################
syntax_error = False #output file is generated at the end, syntax_error is here to keep track of errors


# logicalVariableDict = {} #exclusively logical variables
# arithmeticVairableDict = {} #exlusively arithmetic variables

variableDict = {}

keywordDict = {"ve": 'and', "veya": 'or', "dogru": True, "yanlis": False, '(': '(', ')': ')', "kapa-parantez": ')', "ac-parantez": '(', '-': '-', '+': '+', '*': '*', "eksi": '-', "carpi": '*', "arti": '+', "sifir": 0, "bir": 1, "iki": 2, "uc": 3, "dort": 4, "bes": 5, "alti": 6, "yedi": 7, "sekiz": 8, "dokuz": 9,'0': 0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9}
textNumDict = {"sifir": 0, "bir": 1, "iki": 2, "uc": 3, "dort": 4, "bes": 5, "alti": 6, "yedi": 7, "sekiz": 8, "dokuz": 9}
numericalNumDict = {'0': 0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9}
logicalDict = {"ve": 'and', "veya": 'or', "dogru": True, "yanlis": False}
arithmeticDict = {'-': '-', '+': '+', '*': '*', "eksi": '-', "carpi": '*', "arti": '+', "sifir": 0, "bir": 1, "iki": 2, "uc": 3, "dort": 4, "bes": 5, "alti": 6, "yedi": 7, "sekiz": 8, "dokuz": 9,'0': 0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9}
############################## VARIABLES ##############################

############################## FUNCTIONS START ##############################
############################## FUNCTIONS START ##############################
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

def expressionCalculator(tempString): ##CALCULATES EXPRESSION
    tempString = tempString.replace('*', "carpi").replace('+', "arti").replace('-', "eksi")
    tempList = tempString.split()
    while "nokta" in tempList:
        noktaIndex = tempList.index("nokta")
        try:
            noktaString = tempList[noktaIndex-1] + ' ' + tempList[noktaIndex] + ' ' + tempList[noktaIndex+1]
            tempList[noktaIndex-1] = noktaString
            del tempList[noktaIndex]
            del tempList[noktaIndex]
        except:
            syntax_error = True
    for tempValueString in tempList:
        whatType = None
        if tempValueString in ["arti", "carpi", "eksi", "ve", "veya"]:
            continue
        else:
            tempValue = valueFinalizer(tempValueString)
            if tempValue != None:
                if tempValue[1] == "arr" and (whatType == None or whatType == "arr"):
                    whatType == "arr"
                elif tempValue[1] == "log" and (whatType == None or whatType == "log"):
                    whatType = "log"
                else:
                    syntax_error = True
                    break
                tempList[tempList.index(tempValueString)] = tempValue[0]
            else:
                break

    if whatType == "log":
        while "ve" in tempList:
            try:
                veIndex = tempList.index("ve")
                veValue = tempList[veIndex-1] and tempList[veIndex+1]
                tempList[veIndex-1] = veValue
                del tempList[veIndex]
                del tempList[veIndex]
            except:
                syntax_error = True
                break
        while "veya" in tempList:
            try:
                veyaIndex = tempList.index("veya")
                veyaValue = tempList[veyaIndex-1] and tempList[veyaIndex+1]
                tempList[veyaIndex-1] = veyaValue
                del tempList[veyaIndex]
                del tempList[veyaIndex]
            except:
                syntax_error = True
                break

    if whatType == "arr":
        while "carpi" in tempList:
            try:
                carpiIndex = tempList.index("carpi")
                carpiValue = tempList[carpiIndex-1] * tempList[carpiIndex+1]
                tempList[carpiIndex-1] = carpiValue
                del tempList[carpiIndex]
                del tempList[carpiIndex]
            except:
                syntax_error = True
                break        
        while "eksi" in tempList:
            try:
                eksiIndex = tempList.index("eksi")
                eksiValue = tempList[eksiIndex-1] - tempList[eksiIndex+1]
                tempList[eksiIndex-1] = eksiValue
                del tempList[eksiIndex]
                del tempList[eksiIndex]
            except:
                syntax_error = True
                break
        while "arti" in tempList:
            try:
                artiIndex = tempList.index("arti")
                artiValue = tempList[artiIndex-1] + tempList[artiIndex+1]
                tempList[artiIndex-1] = artiValue
                del tempList[artiIndex]
                del tempList[artiIndex]
            except:
                syntax_error = True
                break
    return tempList


def expressionSyntaxChecker(expressionString): #takes expressionFinder as input
    global syntax_error
    expressionString.replace("ac-parantez", '(').replace("kapa-parantez", ')')
    if expressionString != None:
        expressionList = expressionString.split()

        while syntax_error == False and len(expressionList)>0:
            if ('(' or ')') in expressionList:
                try:
                    closeParanIndex = expressionList.index(')')
                    openParanIndex = closeParanIndex
                    while expressionList[openParanIndex] != '(':
                        openParanIndex-=1
                    tempString = ' '.join(expressionList[openParanIndex+1:closeParanIndex])
                except:
                    syntax_error = True
                    break

                if syntax_error == False:
                    tempListValue = expressionCalculator(tempString)
                    if len(tempListValue) == 1:
                        openParanIndex = tempListValue[0]
                        for i in range(closeParanIndex-openParanIndex):
                            del expressionList[openParanIndex+1]
                    else:
                        syntax_error = True
            else:
                tempString  = ' '.join(expressionList)
                if syntax_error == False:
                    tempListValue = expressionCalculator(tempString)
                    if len(tempListValue) == 1:
                        expressionList.clear()
                        expressionList.append(tempListValue[0])
                    else:
                        syntax_error = True
        if len(expressionList) == 1:
            return expressionList[0]
        else:
            syntax_error = True
            return None

        #     if syntax_error == False:
        #         tempString = tempString.replace('*', "carpi").replace('+', "arti").replace('-', "eksi")
        #         tempList = tempString.split()
        #         while "nokta" in tempList:
        #             noktaIndex = tempList.index("nokta")
        #             try:
        #                 noktaString = tempList[noktaIndex-1] + ' ' + tempList[noktaIndex] + ' ' + tempList[noktaIndex+1]
        #                 tempList[noktaIndex-1] = noktaString
        #                 del tempList[noktaIndex]
        #                 del tempList[noktaIndex]
        #             except:
        #                 syntax_error = True
        #         for tempValueString in tempList:
        #             whatType = None
        #             if tempValueString in ["arti", "carpi", "eksi", "ve", "veya"]:
        #                 continue
        #             else:
        #                 tempValue = valueFinalizer(tempValueString)
        #                 if tempValue != None:
        #                     if tempValue[1] == "arr" and (whatType == None or whatType == "arr"):
        #                         whatType == "arr"
        #                     elif tempValue[1] == "log" and (whatType == None or whatType == "log"):
        #                         whatType = "log"
        #                     else:
        #                         syntax_error = True
        #                         break
        #                     tempList[tempList.index(tempValueString)] = tempValue[0]
        #                 else:
        #                     break

        #         if whatType == "log":
        #             while "ve" in tempList:
        #                 try:
        #                     veIndex = tempList.index("ve")
        #                     veValue = tempList[veIndex-1] and tempList[veIndex+1]
        #                     tempList[veIndex-1] = veValue
        #                     del tempList[veIndex]
        #                     del tempList[veIndex]
        #                 except:
        #                     syntax_error = True
        #                     break
        #             while "veya" in tempList:
        #                 try:
        #                     veyaIndex = tempList.index("veya")
        #                     veyaValue = tempList[veyaIndex-1] and tempList[veyaIndex+1]
        #                     tempList[veyaIndex-1] = veyaValue
        #                     del tempList[veyaIndex]
        #                     del tempList[veyaIndex]
        #                 except:
        #                     syntax_error = True
        #                     break

        #         if whatType == "arr":
        #             while "carpi" in tempList:
        #                 try:
        #                     carpiIndex = tempList.index("carpi")
        #                     carpiValue = tempList[carpiIndex-1] * tempList[carpiIndex+1]
        #                     tempList[carpiIndex-1] = carpiValue
        #                     del tempList[carpiIndex]
        #                     del tempList[carpiIndex]
        #                 except:
        #                     syntax_error = True
        #                     break        
        #             while "eksi" in tempList:
        #                 try:
        #                     eksiIndex = tempList.index("eksi")
        #                     eksiValue = tempList[eksiIndex-1] - tempList[eksiIndex+1]
        #                     tempList[eksiIndex-1] = eksiValue
        #                     del tempList[eksiIndex]
        #                     del tempList[eksiIndex]
        #                 except:
        #                     syntax_error = True
        #                     break
        #             while "arti" in tempList:
        #                 try:
        #                     artiIndex = tempList.index("arti")
        #                     artiValue = tempList[artiIndex-1] + tempList[artiIndex+1]
        #                     tempList[artiIndex-1] = artiValue
        #                     del tempList[artiIndex]
        #                     del tempList[artiIndex]
        #                 except:
        #                     syntax_error = True
        #                     break 
        
        # temp








# def expressionSyntaxChecker(expressionString): #takes expressionFinder as input
#     global syntax_error
#     expressionString.replace("ac-parantez", '(').replace("kapa-parantez", ')')
#     if expressionString != None:
#         expressionList = expressionString.split()

#         while syntax_error == False and len(expressionList)>1:
#             if ('(' or ')') in expressionList:
#                 try:
#                     closeParanIndex = expressionList.index(')')
#                     openParanIndex = closeParanIndex
#                     while expressionList[openParanIndex] != '(':
#                         openParanIndex-=1
#                     tempString = ' '.join(expressionList[openParanIndex+1:closeParanIndex])
#                     tempString = tempString.replace('*', "carpi").replace('+', "arti")
#                     tempList = re.split("arti|carpi|-|eski|ve|veya", tempString)
                    
#                     while "nokta" in tempList:
#                         noktaIndex = tempList.index("nokta")
#                         try:
#                             noktaString = tempList[noktaIndex-1] + ' ' + tempList[noktaIndex] + ' ' + tempList[noktaIndex+1]
#                             tempList[noktaIndex-1] = noktaString
#                             del tempList[noktaIndex]
#                             del tempList[noktaIndex]
#                         except:
#                             syntax_error = True
                    
#                     for tempValueString in tempList:
#                         tempValue = valueFinalizer(tempValueString)
#                         if tempValue != None




#                     tempString = ' '.join(tempList)

#                 except:
#                     syntax_error = True
            
            


            






#     global syntax_error
#     if expressionString == None:
#         pass
#     else:
#         expressionList = expressionString.split()
#         # orgExpressionList = expressionString.split()
#         indx = 0
#         whatType = 0 # if whatType is 0 nothing is assigned yet if 1 arr if 2 log if 3 syntax_error = True
#         while indx < len(expressionList):
#             if whatType == 3:
#                 syntax_error = True
#             if syntax_error == False:
#                 current = expressionList[indx]
#                 if current in ["ac-parantez", '(']:
#                     del expressionList[indx]
#                     indx-=1
#                 elif current in ["kapa-parantez", ')']:
#                     del expressionList[indx]
#                     indx-=1
#                 elif current in variableDict:
#                     if variableDict[current][1] == "log" and (whatType == 0 or whatType == 2):
#                         whatType = 2
#                     elif variableDict[current][1] == "arr" and (whatType == 0 or whatType == 1):
#                         whatType = 1
#                     else:
#                         whatType = 3
#                 elif current in textNumDict or current in numericalNumDict:
#                     if whatType == 0 or whatType == 1:
#                         whatType = 1
#                     else:
#                         whatType = 3
#                 elif current in ["dogru", "yanlis"]:
#                     if whatType == 0 or whatType == 2:
#                         whatType = 2
#                     else:
#                         whatType = 3  
#                 elif current in ["eksi", '-', "carpi", '*', "arti", '+']:
#                     if whatType == 0 or whatType == 1:
#                         whatType = 1
#                     else:
#                         whatType = 3
#                     del expressionList[indx]
#                     indx-=1
#                 elif current in ["ve", "veya"]:
#                     if whatType == 0 or whatType == 2:
#                         whatType = 2
#                     else:
#                         whatType = 3
#                     del expressionList[indx]
#                     indx-=1

#                 indx+=1
#             else:
#                 break         
#         print("whatType"+ str(whatType))
# ############################################################
#         print(expressionList)
#         if whatType == 1:
#             for currentString in expressionList:
#                 if currentString in textNumDict or currentString in numericalNumDict:
#                     pass
#                 elif currentString == "nokta":
#                     currIndx = expressionList.index(currentString)
#                     if currIndx > 1 and currIndx < len(expressionList)-2:
#                         if expressionList[currIndx-2] in textNumDict or expressionList[currIndx-1] in textNumDict or expressionList[currIndx+1] in textNumDict or expressionList[currIndx+2] in textNumDict:
#                             syntax_error = True
#                     elif len(expressionList)<3:
#                         syntax_error = True
#                     elif len(expressionList) == 3:
#                         if currIndx != 1 or expressionList[0] in textNumDict or expressionList[2] in textNumDict:
#                             syntax_error = True
#                     elif currIndx == 1 and len(expressionList)> 3:
#                         if expressionList[0] in textNumDict or expressionList[2] in textNumDict or expressionList[3] in textNumDict:
#                             syntax_error = True
#                     elif currIndx == (len(expressionList)-2) and len(expressionList >3):
#                         if expressionList[-1] in textNumDict or expressionList[-3] in textNumDict or expressionList[-4] in textNumDict:
#                             syntax_error = True
#                 elif '.' in currentString:
#                     try:
#                         float(currentString)
#                     except:
#                         syntax_error = True
#                 elif currentString in variableDict and variableDict[currentString][1] == "arr":
#                     pass
#                 else:
#                     syntax_error = True 
#         elif whatType == 2:
#             for currentString in expressionList:
#                 if currentString in ["dogru", "yanlis"]:
#                     pass
#                 elif currentString in variableDict and variableDict[currentString][1] == "log":
#                     pass
#                 else:
#                     syntax_error = True
#         elif whatType == 3:
#             syntax_error = True
# ##########################################################################################
        

#         if syntax_error == False:
#             indexOpen = -1
#             indexClose = 0
#             paranList = expressionString.split()
#             while len(paranList) < -indexOpen and len(paranList) < indexClose +1:
#                 pass
#                 indexOpen-=1
#                 indexClose+=1


        # if syntax_error == False:
        #     for indx4 in range(len(openParanIndex)):
        #         tempList = expressionList[openParanIndex[-indx4-1]:closeParanIndex[indx4]+1]
        #         print("temp list is" + str(tempList))

        # if len(openParanIndex) != len(closeParanIndex):
        #     syntax_error = True


############################## FUNCTIONS END ##############################
############################## FUNCTIONS END ##############################


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

        print(syntax_error)
        inputLine = linesList[index]
        print(inputLine)

        if syntax_error == True:
            break
        elif (index == anaIndex) or (index == yeniIndex) or (index == sonucIndex):
            continue
        elif index < yeniIndex: #while inside                                       ANADEGISKENLER
            variableAndExpressionList = variableAndExpressionFinder(inputLine)
            if variableAndExpressionList[0] not in variableDict:
                variableDict[variableAndExpressionList[0]] = valueFinalizer(variableAndExpressionList[1])
            else:
                syntax_error = True
            print("AnaDegiskenSyntax"+ str(syntax_error))
        elif index < sonucIndex: #while inside YeniDegiskenler
            variableAndExpressionList = variableAndExpressionFinder(inputLine)
            if None not in variableAndExpressionList:
                if variableAndExpressionList[0] not in variableDict:
                    variableDict[variableAndExpressionList[0]] = expressionSyntaxChecker(variableAndExpressionList[1])
                else:
                    syntax_error = True
        else: #while inside sonuc statement
            expressionSyntaxChecker(inputLine)
    print(syntax_error)

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
