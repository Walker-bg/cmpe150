
x = int(input())
y = int(input())
g = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE


######################## ASTROID MATRIX CREATOR ########################

astroids=[]
oneLineAstroids=[]
for i in range(y):                                  ####Creates a matrix about astroids
    oneLineAstroids.append(1)                       ##### 1 if there is an astroid at that pos
for i in range(x):                                  ##### 0 if not
    astroids.append(oneLineAstroids)

######################## ASTROID MATRIX CREATOR ########################



######################## MY VARIABLES ########################

lost=False
#
if y%2:
    shipPos = (y//2)+1
else:
    shipPos = y//2
#
timer=0
#
movement=0 ###times astroids move down

######################## MY VARIABLES ########################



######################## INITIAL VIEW ########################

for i in range(x):                          #### Printing the initial view
    for j in range(y):                      #  
        if astroids[i][j] == 1:             #
            print('*', end='')              #
        else:                               #
            print(' ', end='')              #
    print('')                               #  printing the astroids
for ij in range(g):
    print(' '*(y-1), end='')
    print(' ')                               # printing the space from the astroids to the ship
print(' '*(shipPos-1), end='')
print('@')                                  #printing the pos of the ship 
print('-'*72)

######################## INITIAL VIEW ########################







######################## GAME LOOP START ########################
######################## GAME LOOP START ########################
######################## GAME LOOP START ########################



while lost==False:                          ##### Game Starting loop

    print("Choose your action!")
    action = input()                #######Inputting and formatting the action
    action = action.lower()



    if action == "left" and shipPos>1:              #### left and right action getter
        shipPos -= 1 
    elif action == "right":                 
        shipPos += 1

        

####################################### If the action is fire:::::


    if action == "fire":
        for ijk in range(g):  
            for i in range(movement):     ####### modified printer code prints for g (empty space) times
                print(' '*(y-1), end='')
                print(' ')                               ####### modified printer code prints for g (empty space) times
            for i in range(x):                                  ####Bullet scene printer
                for j in range(y):
                    if astroids[i][j] == 1:
                        print('*', end='')
                    else:
                        print(' ', end='')
                print('')
            for ij in range(g):                 #####Bullet line printer
                if ij == (g-ijk-1): 
                    print(' '*(shipPos-1), end='')      
                    print('|')
                else:
                    print(' '*(y-1), end='')
                    print(' ')
            print(' '*(shipPos-1), end='')
            print('@')
            print('-'*72)



        ############################### ASTROID MATRIX UPDATER ###############################
        
        for i in range(x):
            if astroids[i][shipPos-1] == 1:
                astroids[i][shipPos-1] = 0
                break
            
    
        ############################### ASTROID MATRIX UPDATER ###############################




    ############################### TIME UPDATER ###############################
    timer +=1
    if timer%5==0:
        movement+=1
        g-=1

    ############################### TIME UPDATER ###############################


 
    ############################### GAME END ###############################

    for i in range(x):
        if 1 in astroids[i]:
            pass
        else:
            g+=1
            del astroids[i]




    ############################### FINAL SCENE PRINTER ###############################
    for i in range(movement):
        print(' '*(y-1), end='')
        print(' ')
    for i in range(x):
        for j in range(y):
            if astroids[i][j] == 1:
                print('*', end='')
            else:
                print(' ', end='')
        print('')

    for ij in range(g):
        print(' '*(y-1), end='')
        print(' ')

    print(' '*(shipPos-1), end='')
    print('@')
    print('-'*72)

    ############################### FINAL SCENE PRINTER ###############################







# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
