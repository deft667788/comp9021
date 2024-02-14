# Written by *** for COMP9021
#
# Implements three functions:
# - binary_lunar_addition(number_1, number_2)
#   that lunarly (or is it lunatically?) adds number_2 to number_1;
# - lunar_addition(*numbers)
#   that lunarly adds all arguments;
# - binary_lunar_multiplication(multiplicand, multiplier)
#   that lunarly multiplies multiplicand by multiplier.
#
# Both operations are discussed at
# https://www.youtube.com/watch?v=cZkGeR9CWbk
# Watch it!
#
# Essentially, lunar addition and lunar multiplication
# are like standard addition and multiplication, except that:
# - the lunar sum of two digits is the largest of both digits;
# - the lunar product of two digits the smallest of both digits.
#
# You can assume that the function arguments are exactly as expected,
# namely, positive numbers (possibly equal to 0).

def binary_lunar_addition(number_1, number_2):
    a=(number_1)
    b=(number_2)
    result=0
    
    while True:
        if a==0 and b==0:
            break
        a, a1=divmod(a,10)
        b, b1=divmod(b,10)
        result = result*10+max(a1,b1)


    result=list(str(result))
    result.reverse()
    result=int(''.join(str(symbol) for symbol in result))
    return result


def lunar_addition(*numbers):
    result=0
    while any(numbers):    #any means there are some numbers is not 0
        pre_digits=[]
        for i in numbers:
            pre_digits.append(i//10)

        last_digits=[]
        for i in numbers:
            last_digits.append(i%10)

        result=result*10+max(last_digits)
        numbers=pre_digits
    
    result=list(str(result))
    result.reverse()
    result=int(''.join(str(symbol) for symbol in result))

    return result





def binary_lunar_multiplication(multiplicand, multiplier):
    result = 0
    numbers=[]
    b=multiplier
    
    for i,b1 in enumerate(str(b)[::-1]):
        a=multiplicand
        line=""
        for j,a1 in enumerate(str(a)[::-1]):
            
            line+=str(min(int(b1),int(a1)))
            
        numbers.append(int(line[::-1]+i*'0'))
    result=lunar_addition(*numbers)
    return result
