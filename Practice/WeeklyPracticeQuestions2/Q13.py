def reverseNumPrinter(num):
    if num == 0:
        print()
        return
    if num != None:
        print(num, end=' ')
        return reverseNumPrinter(num-1)

reverseNumPrinter(1)
reverseNumPrinter(2)
reverseNumPrinter(3)
reverseNumPrinter(4)
reverseNumPrinter(5)
reverseNumPrinter(6)
reverseNumPrinter(49)
