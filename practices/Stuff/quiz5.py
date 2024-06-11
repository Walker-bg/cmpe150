import timeit

def check_prime():
    n = int(input())
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    
    start = timeit.default_timer()

    x = 2stop = timeit.default_timer()
    prime = None
    if n == 1:
        prime = False
        print(n, "is not a prime number!")

    while x**2 <= n:
        if n % x == 0:
            print(n, "is not a prime number!")
            prime = False
            break
        x += 1
    if prime != False:
        print(n, "is a prime number!")


    stop = timeit.default_timer()
    print('Time: ', stop - start)
    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
    return


check_prime()