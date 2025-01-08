def CountNoOfSetBits(n):
    ctr = 0
    while n > 1:
        if n % 2 == 1:
            ctr += 1
        n = n // 2
    if n == 1:
        ctr += 1
    return ctr

def CountNoOfSetBits(n):
    ctr = 0
    while n > 1:
        ctr += n & 1
        n = n >> 1
    return ctr

def CountNoOfSetBits(n):
    ctr = 0
    while n != 0:
        n = n & (n - 1)
        ctr += 1
    return ctr  