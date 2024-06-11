def is_valid(bin_str):
    for i in range(len(bin_str) - 1):
        if(bin_str[i] == '1' and bin_str[i+1] == '1'):
            return False
    return True


def rec_consecutive_ones(n, _str):
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    if n == 0:
        print(_str)
        return

    if len(_str) != 0:
        if _str[-1] == '0':
            return rec_consecutive_ones(n-1, _str + '0'), rec_consecutive_ones(n-1, _str + '1')
        else:
            return rec_consecutive_ones(n-1, _str + '0')
    else:
        return rec_consecutive_ones(n-1, _str + '0'), rec_consecutive_ones(n-1, _str + '1') 
    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE


a = int(input())
rec_consecutive_ones(a, '')