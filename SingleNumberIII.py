def SingleNumberIII(nums):
    d = {}
    res = []
    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for i in d:
        if d[i] == 1:
            res.append(i)
    return res
