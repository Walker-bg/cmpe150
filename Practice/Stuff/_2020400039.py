
def read_list(param):
    p = param.replace(',', '')
    p = p[1:-1]
    li = p.split()
    while('' in li):
        li.remove('')
    li = [int(elem) if '.' not in elem else float(elem) for elem in li]
    return li


lst = read_list(input())


def find_sub(input_list):
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    if len(input_list)>0:
        maxSum = min(input_list)-1
        for x in range(len(input_list) + 1):
            for i in range(x, len(input_list) + 1):
                if input_list[x:i]==[]:
                    continue
                else:
                    tempSum = 0
                    for ij in range(len(input_list[x:i])):
                        tempSum = tempSum + input_list[x:i][ij]                        
                    if tempSum > maxSum:
                        maxList = input_list[x:i].copy()
                        maxSum = tempSum
    else:
        maxList=[]
    print(maxList)
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
    return


find_sub(lst)