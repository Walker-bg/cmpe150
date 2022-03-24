def reverseOrder(inString, n=-1):
    if len(inString) == -n:
        print(inString)
        return

    if inString[n] != ' ':
        return reverseOrder(inString, n-1)
    else:
        print(inString[n+1:], end = ' ')
        return reverseOrder(inString[:n], )


reverseOrder("Hello my name is Walker")
reverseOrder("hello")
reverseOrder("h")
reverseOrder("hello how are you doing?")