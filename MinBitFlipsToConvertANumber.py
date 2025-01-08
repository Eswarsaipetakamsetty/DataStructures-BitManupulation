def MinBitFlips(start, goal):
    ans = start ^ goal
    ctr = 0
    for i in range(32):
        if ans & (1 << i):
            ctr += 1
    return ctr