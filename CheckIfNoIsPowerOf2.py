def Check(n):   #check whether n is power of 2 or not
    if n & (n - 1) == 0:
        return True
    return False
