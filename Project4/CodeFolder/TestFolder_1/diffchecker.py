for x in range(1,17):
    orgfilename = "output"+str(x)+".txt"
    myfilename = "myoutput"+str(x)+".txt"
    org = open(orgfilename, 'r')
    my = open(myfilename, 'r')
    orgfile = org.read()
    myfile = my.read()
    if orgfile == myfile:
        print(x,'ok')
    else: print(x,'no ok')
    org.close()
    my.close()