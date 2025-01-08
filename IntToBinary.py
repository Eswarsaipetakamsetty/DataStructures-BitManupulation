def ConvertToBinary(n: int) -> str:
    res = ""
    while n!= 1:
        if n%2 == 1:
            res += '1'
        else:
            res += '0'
        res //= 2
    return res[-1:-1:-1]
