
n = int(input())


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
def h(numb):
    if numb<=1:
        return 1
    elif numb%2==0:
        return h(numb-2)*numb
    elif numb%2==1:
        return h(numb-2)+numb
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

print(h(n))

