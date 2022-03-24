
def input_to_list(_str):
    str_lst = _str.split()
    if(len(str_lst) > 0):
        return [int(elem) for elem in str_lst]
    else:
        return []


def find_difference(lst1, lst2):
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
    return


input_str1 = input()
input_str2 = input()
input_lst1 = input_to_list(input_str1)
input_lst2 = input_to_list(input_str2)
find_difference(input_lst1, input_lst2)

