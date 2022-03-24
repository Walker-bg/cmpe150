

def hw2():
    str_input = "      h h h    "
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

    strList = str_input.split()
    lenght = len(strList)
    if lenght == 0:
        print("No words")
    elif lenght == 1:
        print("One word")
        print(strList[0])
    elif lenght == 2:
        print("Two words")
        print(strList[0], end = ' ')
        print(strList[1])
    else:
        print(str(lenght) + " words!")
        print(strList[0], end = ' ')
        print(strList[-1])

    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
    return


if __name__ == "__main__":
    hw2()
