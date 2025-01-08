def ConvertToDecimal(s):
    l = len(s)
    res = 0
    for i in range(l-1,-1, -1):
        if s[i] == '1':
            res += 2**i
    return res