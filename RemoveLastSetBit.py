def RemoveLastSetBit(n):
    return n & (n - 1)

"""
    84 = 1 0 1 0 1 0 0
    83 = 1 0 1 0 0 1 1
&   ___________________
         1 0 1 0 0 0 0
    -------------------

    n & n- 1
"""