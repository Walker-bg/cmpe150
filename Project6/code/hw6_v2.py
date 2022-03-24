inputFile = open('crime_scene.txt', 'r')
max_weight, max_time = map(int, inputFile.readline().rstrip('/n').split())
num_evidence = int(inputFile.readline().rstrip('/n'))
evidenceDict = {}
ev_Idies = []
lastSolution = None
solutionsList = []

for i in range(num_evidence): #takes inputs and puts them in a dictionary
    ev_Id, ev_weight, ev_time, ev_value = map(int, inputFile.readline().rstrip('/n').split())
    ev_Idies.append(ev_Id)
    evidenceDict[ev_Id] = (ev_weight, ev_time, ev_value)

### FUNCTIONS START
def my_sorting_function(someList): #insertion sort 
    marker = 1      #doesn't return, makes changes in the original function
    listLenght = len(someList)
    while marker < listLenght:
        currId = someList.pop(marker)
        for reverseIndex in range(marker-1,-1,-1):
            if currId > someList[reverseIndex]:
                someList.insert(reverseIndex+1, currId)
                break
            elif reverseIndex == 0:
                someList.insert(reverseIndex, currId)
        marker+=1

def solutionGenerator(typ, maxW, maxT, currW=0, currT=0, currVal=0, currentIdiesList = [], n=0):
    global lastSolution, generalMaxValue
    if n == num_evidence:
        if currVal > generalMaxValue and (currT <= maxT and currW <= maxW):
            generalMaxValue = currVal
            lastSolution = [currentIdiesList.copy(), currVal]
        currentIdiesList = []
        return  
    currTuple = evidenceDict[ev_Idies[n]]   
    if typ == 3:
        return solutionGenerator(typ, maxW, maxT, currW+currTuple[0], currT+currTuple[1], currVal+currTuple[2], currentIdiesList + [ev_Idies[n]], n+1), solutionGenerator(typ, maxW, maxT, currW, currT, currVal, currentIdiesList, n+1)
    elif typ == 2:
        return solutionGenerator(typ, maxW, maxT, currW+currTuple[1], currT+currTuple[1], currVal+currTuple[2], currentIdiesList + [ev_Idies[n]], n+1), solutionGenerator(typ, maxW, maxT, currW, currT, currVal, currentIdiesList, n+1)
    elif typ == 1:
        return solutionGenerator(typ, maxW, maxT, currW+currTuple[0], currT+currTuple[0], currVal+currTuple[2], currentIdiesList + [ev_Idies[n]], n+1), solutionGenerator(typ, maxW, maxT, currW, currT, currVal, currentIdiesList, n+1)
### FUNCTIONS END

generalMaxValue = 0
solutionGenerator(1, max_weight, max_weight) #for weight
onlyWeight = open('solution_part1.txt', 'w')
my_sorting_function(lastSolution[0])
onlyWeight.write(str(lastSolution[1])+ '\n'+ ' '.join(list(map(str, lastSolution[0]))))
onlyWeight.close()
print(lastSolution)

generalMaxValue = 0
solutionGenerator(2, max_time, max_time) #for time
onlyTime = open('solution_part2.txt', 'w')
my_sorting_function(lastSolution[0])
onlyTime.write(str(lastSolution[1])+ '\n'+ ' '.join(list(map(str, lastSolution[0]))))
onlyTime.close()
print(lastSolution)

generalMaxValue = 0
solutionGenerator(3, max_weight, max_time) #for both
bothWeightandTime = open('solution_part3.txt', 'w')
my_sorting_function(lastSolution[0])
bothWeightandTime.write(str(lastSolution[1])+ '\n'+ ' '.join(list(map(str, lastSolution[0]))))
bothWeightandTime.close()
print(lastSolution)

