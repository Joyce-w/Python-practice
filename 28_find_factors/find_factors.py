def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """

    factors = [1]
    if num % 2 == 0:
        for fac in range(2, int(num / 2) + 1):
            if num % fac == 0:
                factors.append(fac)
        factors.append(num)
    else:
        for fac in range(2, int(num - 1 / 2) + 1):
            if num % fac == 0:
                factors.append(fac)
        factors.append(num)
    return (factors)
