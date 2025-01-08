def setith(n, i):
    n = n | (1 << i)
    return n

def clearith(n, i):
    n = n & ~(1 << i)