import random
my_list = [random.randint(1, 1001) for i in range(101)]




def my_sorting_function_bubble_sort(someList):
    for i in range(len(someList)):
        for j in range(len(someList)-1):
            if someList[j] > someList[j+1]:
                someList[j], someList[j+1] = someList[j+1], someList[j]

def my_sorting_function_insertion_sort(someList):
    for marker in range(1, len(someList)):
        currentNum = someList.pop(marker)
        for inserter in range(marker, -1, -1):
            if someList[inserter] < currentNum:
                someList.insert(inserter+1, currentNum)
                break
            elif inserter == 0:
                someList.insert(inserter, currentNum)




my_list = [random.randint(1, 1001) for i in range(101)]
true_sorted_mylist = my_list.copy()
true_sorted_mylist.sort()
my_sorting_function_insertion_sort(my_list)

if true_sorted_mylist == my_list:
    print('groovy baby, yeah!')

# print(my_list)
# print(true_sorted_mylist)