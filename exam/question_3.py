# Will be tested only with strictly positive integers for
# total_nb_of_letters and height.
#
# <BLANKLINE> is not output by the program, but
# doctest's way to refer to an empty line.
# For instance,
#    A
#    B
#    C
#    <BLANKLINE>
#    <BLANKLINE>
# means that 5 lines are output: first a line with A,
# then a line with B, then a line with C,
# and then 2 empty lines.
#
# Note that no line has any trailing space.

def f(total_nb_of_letters, height):
    '''
    >>> f(4, 1)
    ABCD
    >>> f(3, 5)
    A
    B
    C
    <BLANKLINE>
    <BLANKLINE>
    >>> f(4, 2)
    AD
    BC
    >>> f(5, 2)
    ADE
    BC
    >>> f(6, 2)
    ADE
    BCF
    >>> f(7, 2)
    ADE
    BCFG
    >>> f(8, 2)
    ADEH
    BCFG
    >>> f(9, 2)
    ADEHI
    BCFG
    >>> f(17,5)
    AJK
    BIL
    CHM
    DGNQ
    EFOP
    >>> f(100, 6)
    ALMXYJKVWHITUFGRS
    BKNWZILUXGJSVEHQT
    CJOVAHMTYFKRWDIPU
    DIPUBGNSZELQXCJOV
    EHQTCFORADMPYBKN
    FGRSDEPQBCNOZALM
    '''
    # INSERT YOUR CODE HERE
    A = 'A'
    add = 0
    output = [[] for _ in range(height)]
    cur_num = 0
    cur_height = list(range(0, height))
    cur_height_idx = 0
    while cur_num < total_nb_of_letters:
        cur_letter = chr(ord(A) + add)
        output[cur_height[cur_height_idx]].append(cur_letter)

        cur_num += 1
        add = (add + 1) % 26
        cur_height_idx = (cur_height_idx + 1) % height
        if cur_height_idx == 0:
            cur_height = cur_height[::-1]

    for idx, line in enumerate(output):
        for letter in line:
            print(letter, end='')
        print()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
