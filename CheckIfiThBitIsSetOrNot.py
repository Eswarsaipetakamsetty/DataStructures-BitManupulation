def checkIthbBit(n, k):
    if n & (n << k):
        return True
    return False

def checkIthBit(n, k):
    if (n >> k) & 1 == 0:
        return False
    return True