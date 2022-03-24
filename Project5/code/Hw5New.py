import re
from decimal import Decimal

############################## VARIABLES ##############################
syntax_error = False #output file is generated at the end, syntax_error is here to keep track of errors


# logicalVariableDict = {} #exclusively logical variables
# arithmeticVairableDict = {} #exlusively arithmetic variables

variableDict = {}

keywordDict = {'Sonuc': None, 'AnaDegiskenler': None, 'YeniDegiskenler': None, 'degeri': None, "olsun": None, "ve": 'and', "veya": 'or', "dogru": True, "yanlis": False, '(': '(', ')': ')', "kapa-parantez": ')', "ac-parantez": '(', '-': '-', '+': '+', '*': '*', "eksi": '-', "carpi": '*', "arti": '+', "sifir": 0, "bir": 1, "iki": 2, "uc": 3, "dort": 4, "bes": 5, "alti": 6, "yedi": 7, "sekiz": 8, "dokuz": 9,'0': 0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9}
textNumDict = {"sifir": 0, "bir": 1, "iki": 2, "uc": 3, "dort": 4, "bes": 5, "alti": 6, "yedi": 7, "sekiz": 8, "dokuz": 9}
numericalNumDict = {'0': 0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9}
logicalDict = {"ve": 'and', "veya": 'or', "dogru": True, "yanlis": False, "True": True, "False": False}
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

def valueFinalizer(valueString):  #returns the appopriate parsed value, if there is a syntax error in the value part, it finds it.
    global syntax_error             #for clean values only
    global index
    global yeniIndex
    global anaIndex
    global sonucIndex
    if valueString != None:
        if valueString in variableDict:
            if index < yeniIndex:
                syntax_error = True
            elif (index == anaIndex) or (index == yeniIndex) or (index == sonucIndex):
                pass
            else:
                if isinstance(variableDict[valueString], tuple) == False:
                    parsedValue = variableDict[valueString]
                    if isinstance(parsedValue, bool):
                        arithmeticOrLogical = 'log'
                    elif (parsedValue in ['False', 'True']):
                        arithmeticOrLogical = 'log'
                        if parsedValue == 'False':
                            parsedValue = False
                        elif parsedValue == 'True':
                            parsedValue = True
                    else:
                        arithmeticOrLogical = 'arr'
                elif variableDict[valueString][1] == 'arr':
                    arithmeticOrLogical = 'arr'
                    parsedValue = variableDict[valueString][0]
                elif variableDict[valueString][1] == 'log':
                    arithmeticOrLogical = 'log'
                    parsedValue = variableDict[valueString][0]
        elif ('E+' in valueString or '-' in valueString or valueString.isdigit() or '.' in valueString or re.search("nokta", valueString) or valueString in numericalNumDict or valueString in textNumDict):
            arithmeticOrLogical = "arr"
            if '.' in valueString:
                try:
                    parsedValue = Decimal(valueString)
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
            elif valueString.isdigit:
                parsedValue = Decimal(valueString)
            elif valueString[1:].isdigit() and valueString[0] == '-':
                parsedValue = Decimal(valueString)
            elif 'E+' in valueString:
                try:
                    parsedValue = Decimal(valueString)
                except:
                    syntax_error = True
            elif variableDict[valueString][1] == 'arr':
                parsedValue = variableDict[valueString][0]

        elif valueString in ["dogru", "yanlis", 'True', "False"]:
            arithmeticOrLogical = "log"
            parsedValue = logicalDict[valueString]

        else:
            syntax_error = True
    if syntax_error == False:   
        return (parsedValue, arithmeticOrLogical)
    else:
        return None


def expressionCalculator(tempString): ##CALCULATES EXPRESSION
    global syntax_error
    tempString = tempString.replace('*', "carpi").replace('+ ', "arti ").replace('- ', "eksi ")
    tempList = tempString.split()

    while "nokta" in tempList:
        print(tempList)
        noktaIndex = tempList.index("nokta")
        try:
            noktaString = tempList[noktaIndex-1] + ' ' + tempList[noktaIndex] + ' ' + tempList[noktaIndex+1]
            tempList[noktaIndex-1] = noktaString
            del tempList[noktaIndex]
            del tempList[noktaIndex]
        except:
            syntax_error = True

    whatType = None
    for tempValueString in tempList:
        print(tempList)
        if tempValueString in ["arti", "carpi", "eksi", "ve", "veya"]:
            continue
        else:
            tempValue = valueFinalizer(tempValueString)
            if tempValue != None:
                if tempValue[1] == "arr" and (whatType == None or whatType == "arr"):
                    whatType = "arr"
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
                if (isinstance(tempList[veIndex-1], bool) and isinstance(tempList[veIndex+1], bool)):
                    veValue = tempList[veIndex-1] & tempList[veIndex+1]
                else:
                    syntax_error = True
                tempList[veIndex-1] = veValue
                del tempList[veIndex]
                del tempList[veIndex]
            except: 
                syntax_error = True
                break
        
        while "veya" in tempList:
            try:
                veyaIndex = tempList.index("veya")
                if isinstance(tempList[veyaIndex-1], bool) and isinstance(tempList[veyaIndex+1], bool):
                    veyaValue = tempList[veyaIndex-1] & tempList[veyaIndex+1]
                else:
                    syntax_error = True
                veyaValue = tempList[veyaIndex-1] | tempList[veyaIndex+1]
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
                carpiValue = Decimal(tempList[carpiIndex-1]) * Decimal(tempList[carpiIndex+1])
                tempList[carpiIndex-1] = carpiValue
                del tempList[carpiIndex]
                del tempList[carpiIndex]
            except:
                syntax_error = True
                break        

        while "eksi" in tempList:
            try:
                eksiIndex = tempList.index("eksi")
                eksiValue = Decimal(tempList[eksiIndex-1]) - Decimal(tempList[eksiIndex+1])
                tempList[eksiIndex-1] = eksiValue
                del tempList[eksiIndex]
                del tempList[eksiIndex]  
            except:
                syntax_error = True
                break

        while "arti" in tempList:
            try:
                artiIndex = tempList.index("arti")
                artiValue = Decimal(tempList[artiIndex-1]) + Decimal(tempList[artiIndex+1])
                tempList[artiIndex-1] = artiValue
                del tempList[artiIndex]
                del tempList[artiIndex]
            except:
                syntax_error = True
                break

    return tempList


def expressionSyntaxChecker(expressionString): #takes expressionFinder as input
    global syntax_error
    expressionString = expressionString.replace("ac-parantez", '(').replace("kapa-parantez", ')')
    if expressionString != None:
        expressionList = expressionString.split()
        while syntax_error == False and len(expressionList)>0:
            print(expressionList)
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
                        expressionList[openParanIndex] = str(tempListValue[0])
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
        if '.' in cleanLine:
            tempSplit = cleanLine.split()
            for something in tempSplit:
                if ('.' in something) and (len(something) != 3):
                    syntax_error = True
        linesList[tempIndex] = cleanLine
        tempIndex+=1

firstTime = 0

if ("AnaDegiskenler" in linesList and "YeniDegiskenler" in linesList and "Sonuc" in linesList): #If every segment is here 
    anaIndex = linesList.index("AnaDegiskenler")  #we can start the loop, else just syntax error  
    yeniIndex = linesList.index("YeniDegiskenler") #Also I store the indices of these segments
    sonucIndex = linesList.index("Sonuc")
    if anaIndex < yeniIndex < sonucIndex:
        for index in range(len(linesList)): #index and inputLine is reassinged for each loop
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
            elif index < sonucIndex: #while inside YeniDegiskenler
                variableAndExpressionList = variableAndExpressionFinder(inputLine)
                if None not in variableAndExpressionList:
                    if variableAndExpressionList[0] not in variableDict:
                        variableDict[variableAndExpressionList[0]] = expressionSyntaxChecker(variableAndExpressionList[1])
                    else:
                        syntax_error = True
            else: #while inside sonuc statement
                if firstTime == 0:
                    expressionSyntaxChecker(inputLine)
                    firstTime +=1
                else:
                    syntax_error = True
    else:
        syntax_error = True

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
