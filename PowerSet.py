def PowerSet(li):
    ans = []
    n = len(li)
    subsets = 1 << n
    for num in range(subsets):
        ls = []
        for i in range(n):
            if num & (1 << i):
                ls.append(li[i])
        ans.append(ls)
    return ans