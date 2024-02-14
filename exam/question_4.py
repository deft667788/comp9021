from itertools import zip_longest


# The carry over of the sum of all units is discarded.
# The carry over of the sum of all multiples of 10 is discarded.
# The carry over of the sum of all multiples of 100 is discarded.
# ...
# Will be tested with at least one argument,
# all arguments being positive integers (possibly equal to 0).

def sum_discarding_carry_overs(*numbers):
    '''
    >>> sum_discarding_carry_overs(0)
    0
    >>> sum_discarding_carry_overs(3, 4)
    7
    >>> sum_discarding_carry_overs(4, 6)
    0
    >>> sum_discarding_carry_overs(7, 5)
    2
    >>> sum_discarding_carry_overs(0, 1, 2, 3)
    6
    >>> sum_discarding_carry_overs(0, 1, 2, 3, 4)
    0
    >>> sum_discarding_carry_overs(0, 1, 2, 3, 4, 5)
    5
    >>> sum_discarding_carry_overs(91, 19)
    0
    >>> sum_discarding_carry_overs(38, 49)
    77
    >>> sum_discarding_carry_overs(58, 59)
    7
    >>> sum_discarding_carry_overs(2314, 5968)
    7272
    >>> sum_discarding_carry_overs(3452, 2324, 36372, 75401)
    6449
    >>> sum_discarding_carry_overs(9054, 3, 3577, 78, 452563)
    454055
    '''
    res = None
    for n in list(numbers):
        if res is None:
            res = n
        else:
            temp_res = res
            res = 0
            while temp_res != 0 or n != 0:
                res *= 10
                cur_digit_res = temp_res % 10
                cur_digit_n = n % 10
                temp_res //= 10
                n //= 10

                cur_digit = (cur_digit_res + cur_digit_n) % 10
                res += cur_digit

        while res > 10 and res % 10 == 0:
            res //= 10

    return res
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE 


if __name__ == '__main__':
    import doctest

    doctest.testmod()
