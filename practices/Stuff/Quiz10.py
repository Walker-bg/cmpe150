
def input_to_list(_str):
    str_lst = _str.split()
    if(len(str_lst) > 0):
        return [int(elem) for elem in str_lst]
    else:
        return []


def sum_2_int_lists(l1, l2, res):
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    if len(l1) == 0:
        print(res)
        return
    res.append(l1[0]+l2[0])
    sum_2_int_lists(l1[1:], l2[1:], res)
    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE


a = input_to_list(input())
b = input_to_list(input())
sum_2_int_lists(a, b, [])
