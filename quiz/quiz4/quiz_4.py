# Written by *** for COMP9021
#
# Call "trinumber" any integer that is the product of
# 3 prime numbers, for instance:
# - 8, equal to 2 x 2 x 2
# - 363, equal to 3 x 11 x 11
# - 455, equal to 5 x 7 x 13
# - 231, equal to 3 x 7 x 11
# - 782, equal to 2 x 17 x 23
#
# Given a trinumber n, call "gap in its decomposition"
# the minimum of
# - the difference between second and first primes
#   in n's decomposition, and
# - the difference between third and second primes
#   in n's decomposition
# (ordering the 3 primes from smallest to largest).
# For instance,
# - the gap in the decomposition of 8 is 0 (2 - 2)
# - the gap in the decomposition of 363 is 0 (11 - 11)
# - the gap in the decomposition of 455 is 2 (7 - 5)
# - the gap in the decomposition of 231 is 4 (7 - 3 or 11 - 7)
# - the gap in the decomposition of 782 is 6 (23 - 17)
#
# Implements a function tri_numbers(n) that outputs:
# - the number of trinumbers at most equal to n included;
# - the largest trinumber at most equal to n included;
# - the maximum gap in the decomposition of trinumbers
#   at most equal to n included;
# - ordered from smallest to largest, the numbers having
#   that maximum gap in their decompositions,
#   together with their decompositions.
#
# You can assume that n is an integer at least equal to 8.
# In the tests, its value won't exceed 50_000_000.

from math import sqrt


def sieve_of_primes_up_to(n):
    sieve = [True] * (n + 1)
    for p in range(2, round(sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve

def tri_numbers(n):
    
    top_number=8
    a=b=c=2
    primes = sieve_of_primes_up_to(n//4+1)
    primes = [index for index,item in enumerate(primes) if index>1 and item]
    from collections import defaultdict
    result = defaultdict(list)
    count = 0
    for i in range(len(primes)):
        first = primes[i]
        list_numbers = []
        if first**3>n:
            break
        for j in range(i,len(primes)):
            second = primes[j]
            if first*second*second>n:
                break
            for k in range(j,len(primes)):
                third = primes[k]
                if first*second*third>n:
                    break
                if first*second*third<=n:
                    count+=1
                    gap=min(second-first,third-second)
                    result[gap].append((first,second,third))
                    
                    
                    if first*second*third>top_number:
                        top_number=first*second*third
                        a,b,c=first,second,third
                        
    if count==1:
        print(f'There is 1 trinumber at most equal to {n}.')
        print(f'The largest one is {top_number}, equal to {a} x {b} x {c}.')
    else:
        print(f'There are {count} trinumbers at most equal to {n}.')
        print(f'The largest one is {top_number}, equal to {a} x {b} x {c}.')
    print()
                
    if result:
        max_gap = max(result.keys())
        print(f'The maximum gap in decompositions is {max_gap}.')
        print(f'It is achieved with:')
        for first,second,third in result[max_gap]:
            max_number = first*second*third
            e,f,g=first,second,third
        
            print(f'  {max_number} = {e} x {f} x {g}')
