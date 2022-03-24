import sys

x=16
orgfilename = "input"+str(x)+".txt"
myfilename = "myoutput"+str(x)+".txt"

sys.stdin = open(orgfilename, "r")
sys.stdout = open(myfilename, "w")

x = int(input())
y = int(input())
g = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
######################## VARIABLES ########################
if y%2:
    shipPos = (y//2)+1
else:
    shipPos = y//2
boardH =x+g
timer=0
lost=False
lossReason=None
firstLooper=0
action=None
score=0
######################## VARIABLES ########################


######################## ASTROID MATRIX CREATOR ########################
board=[]
oneLineAstroids=[]
oneLineSpace=[]                         # 0-> space
for i in range(y):                      # 1-> astroid           
    oneLineSpace.append(0)              # 2-> ship       
for i in range(y):                      # 3-> bullet           
    oneLineAstroids.append(1)
oneLineShip=oneLineSpace.copy()
oneLineShip[shipPos-1]=2
board.append(oneLineShip)
for i in range(g):
    board.append(oneLineSpace.copy())   
for i in range(x):                 
    board.append(oneLineAstroids.copy())
######################## ASTROID MATRIX CREATOR ########################

######################## ASTROID MATRIX UPDATER ########################
# if timesMoved > 1:                  #board mover
#     if 1 in board[0]: 
#         lost=True
#     else:
#         tempBoard=board[0].pop()    
#         board.append(tempBoard)
#         timesMoved-=1

# for i in range(boardH):             #fire updater
#     if board[i][(shipPos-1)] == 1:
#         board[i][(shipPos-1)]=0
#         break
######################## ASTROID MATRIX UPDATER ########################


# ######################## BOARD PRINTER ########################
# for i in range(1,boardH+2):
#     for j in range(y):
#         if board[-i][j]==1:
#              f.write('*',end='')
#         if board[-i][j]==0:
#              f.write(' ',end='')
#         if board[-i][j]==2:
#              f.write('@',end='')
#     print('')
#     print('-'*72)
# ######################## BOARD PRINTER ########################


######################## GAME LOOP START ########################
######################## GAME LOOP START ########################

while lost==False:  #game starting loop
                            
    if firstLooper!=0:
        print("Choose your action!")
        action = input()                        #inputting and formatting the action
        action = action.lower()
        timer+=1


    tempShipIndex = board[0].index(2)

    ######################## LEFT AND RIGHT INDEX UPDATER ########################
    if action == 'left' and tempShipIndex!=0:
        board[0][tempShipIndex]=0
        board[0][tempShipIndex-1]=2

    if action == 'right' and tempShipIndex!=(y-1):
        board[0][tempShipIndex]=0
        board[0][tempShipIndex+1]=2
    ######################## LEFT AND RIGHT INDEX UPDATER ########################


    ######################## FIRE SCENE PRINTER ########################
    if action == 'fire':
        for ij in range(boardH):
            if board[ij+1][tempShipIndex]==0: #scene updater and printer
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

        for i in range(boardH+1):             #fire updater
            if board[i][tempShipIndex] == 1:
                board[i][tempShipIndex]=0
                score+=1
                break         
    ######################## FIRE SCENE PRINTER ########################

    if action == 'exit':     #exit action
        lost=True

    ######################## ASTROID MOVER AND GAME ENDER ########################
    if lost == False: 
        if firstLooper!=0:
            if (timer)%5==0 and (1 in board[1]):
                lost=True
                print("GAME OVER")  
            if timer%5==0 and (1 not in board[1]):
                del board[1]
                board.append(oneLineSpace.copy())
        
        if score == (x*y):              #If score equals initial number of astroids game ends
            print("YOU WON!")
            lost=True
    ######################## ASTROID MOVER AND GAME ENDER ########################


    ######################## FINAL BOARD PRINTER ########################
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
    ######################## FINAL BOARD PRINTER ########################

    if lost==True:
        print("YOUR SCORE: "+ str(score))

    if firstLooper==0:
        firstLooper+=1


sys.stdout.close()

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE