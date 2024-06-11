t = [(1,2,3),(4,5,6)]


last_list = []
temp_sum = 0
for i in t:
    temp_sum = 0
    for num in t[i]:
        temp_sum = temp_sum + t[i][num]

    avg = temp_sum / num
    avg = format(avg, '.2f')
    print(avg)