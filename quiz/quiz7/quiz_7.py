# Written by *** for COMP9021
#
# Watch https://www.youtube.com/watch?v=7DHE8RnsCQ8
#
# Implements a function centrifuge(n, k) that takes
# as first argument an integer n at least equal to 2,
# as second argument an integer k between 0 and n included,
# and returns True or False depending on whether it is
# possible to balance k identical test tubes
# in an n-hole centrifuge, respectively.



import sys

sys.setrecursionlimit(10000000)

from math import sqrt


def sieve_of_primes_up_to(n):
    sieve = [True] * (n + 1)
    for p in range(2, round(sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve


def centrifuge(n, k):
    if k == 0 or k == n:
        return True
    primes = sieve_of_primes_up_to(n)
    if primes[n]:
        return False
    primes_factors = []
    for i in range(2, n // 2 + 1):
        if primes[i] and n % i == 0:
            primes_factors.append(i)
    
    # primes_factors = prime_factor(n, primes)
    # return primes_factors

    return centrifuge_recursion(k, primes_factors) and centrifuge_recursion(n - k, primes_factors)


def centrifuge_recursion(k, factors):
    # base case
    if k == 1:
        return False
    while k > 1:
        if k in factors:
            return True
        for i in range(len(factors)):
            if k % factors[i] == 0:
                return True

        # recursive case
        return centrifuge_recursion(k - factors[0], factors)
    return False    
    # centrifuge2(k, prime_factors)
