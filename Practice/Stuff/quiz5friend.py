import timeit

def check_prime():
    n = int(input())
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    start = timeit.default_timer()


    for e in range(2, int(n**(1/2)) + 1):
        if n % e == 0:
            print(n, 'is not a prime number!')
            break
        else:
            continue
    else:
        print(n, 'is a prime number!')

    end = timeit.default_timer()
    print('Time:', end-start)
    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
    return


check_prime()



