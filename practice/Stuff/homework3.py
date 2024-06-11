def hw3():
    cumulative_sum = 0
    n = int(input())
    x = int(input())
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    
    numeralsList = []
    
    if x == 0: 
        pass
    else:    
        for k in range(x):
            numeralsList.append(int(input()))
        
        numeralsList.reverse()
        tempSum = 0
        y = 0

        for i in range(n):
            tempSum = tempSum + (numeralsList[y] * (10**i))
            cumulative_sum = cumulative_sum + tempSum

            y += 1
            if i == x-1:
                y  = 0
                
    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
    print(cumulative_sum)
    return cumulative_sum


if __name__ == "__main__":
    hw3()

