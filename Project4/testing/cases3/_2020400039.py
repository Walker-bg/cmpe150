
x = int(input())
y = int(input())
g = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
if y%2:
    shipPos = (y//2)+1
else:
    shipPos = y//2
boardH, timer, lost, lossReason, firstLooper, action, score = (x+g), 0, False, None, 0, None, 0
board=[]
oneLineAstroids=[]
oneLineSpace=[]
for i in range(y):
    oneLineSpace.append(0)
for i in range(y):
    oneLineAstroids.append(1)
oneLineShip=oneLineSpace.copy()
oneLineShip[shipPos-1]=2
board.append(oneLineShip)
for i in range(g):
    board.append(oneLineSpace.copy())
for i in range(x):
    board.append(oneLineAstroids.copy())
while lost==False:
    if firstLooper!=0:
        print("Choose your action!")
        action = input()
        action = action.lower()
        timer+=1
    tempShipIndex = board[0].index(2)
    if action == 'left' and tempShipIndex!=0:
        board[0][tempShipIndex]=0
        board[0][tempShipIndex-1]=2
    if action == 'right' and tempShipIndex!=(y-1):
        board[0][tempShipIndex]=0
        board[0][tempShipIndex+1]=2
    if action == 'fire':
        for ij in range(boardH):
            if board[ij+1][tempShipIndex]==0:
                board[ij+1][tempShipIndex]=3
                for i in range(1,boardH+2):
                    for j in range(y):
                        if board[-i][j]==1:
                            print('*',end='')
                        if board[-i][j]==0:
                            print(' ',end='')
                        if board[-i][j]==2:
                            print('@',end='')
                        if board[-i][j]==3:
                            print('|',end='')
                    print('')
                print('-'*72)
                board[ij+1][tempShipIndex]=0
            else:
                break
        for i in range(boardH+1):
            if board[i][tempShipIndex] == 1:
                board[i][tempShipIndex]=0
                score+=1
                break
    if action == 'exit':
        lost=True
    if lost == False:
        if firstLooper!=0:
            if (timer)%5==0 and (1 in board[1]):
                lost=True
                print("GAME OVER")
            if timer%5==0 and (1 not in board[1]):
                del board[1]
                board.append(oneLineSpace.copy())
        if score == (x*y):
            print("YOU WON!")
            lost=True
    for i in range(1,boardH+2):
        for j in range(y):
            if board[-i][j]==1:
                print('*',end='')
            if board[-i][j]==0:
                print(' ',end='')
            if board[-i][j]==2:
                print('@',end='')
        print('')
    print('-'*72)
    if lost==True:
        print("YOUR SCORE: "+ str(score))
    if firstLooper==0:
        firstLooper+=1
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
