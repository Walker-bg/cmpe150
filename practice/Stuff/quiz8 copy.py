
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
    n = len(input_list)
    if n == 0:
        print(input_list)
    else:
        maxSum = input_list[0]
        start = 0
        end = 0
        for i in range(0, n):
            tempSum = 0
            for j in range(i, n):
                tempSum += input_list[j]
                if tempSum > maxSum:
                    start = i
                    end = j
                    maxSum  = tempSum 
        print(input_list[start:end+1])
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
    return


find_sub(lst)