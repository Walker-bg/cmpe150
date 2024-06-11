edgeL = 0
while edgeL <=1:
    edgeL = int(input())

print('*'*edgeL)
line = list(' '*edgeL)
line[0], line[-1] = '*', '*'
for i in range(1, edgeL-1):
    line[i] = '\\'
    print(''.join(line))
    line[i] = ' '
print('*'*edgeL)
