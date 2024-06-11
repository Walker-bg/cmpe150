def almost_equal(a, b):
    epsilon = 0.0001
    if a>b:
        if a-b <= epsilon:
            return True
    else:
        if b-a <= epsilon:
            return True

