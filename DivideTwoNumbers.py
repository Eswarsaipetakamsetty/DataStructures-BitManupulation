def DivideTwoNumbers(dividend, divisor):
    if dividend == divisor:
        return True
    sign = True
    if dividend >= 0 and divisor < 0:
        sign = False
    if dividend < 0 and divisor > 0:
        sign = False
    
    n = abs(dividend)
    d = abs(divisor)
    ans = 0
    while n >= d:
        ctr = 0
        while n >= d << ctr + 1:
            ctr += 1
        ans += 1 << ctr
        n = n - (d * (1 << ctr))
    
    if ans > 2**31 and sign == True:
        return float('inf')
    if ans >= 2**31 and sign == False:
        return -float('inf')
    
    return ans if sign else -ans
        