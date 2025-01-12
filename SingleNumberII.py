def singleNumberII(nums):   #bruiteforce
    result = 0
    n = len(nums)
    for bitind in range(0, 32):
        ctr = 0
        for i in range(0, n):
            if nums[i] & (1 << bitind):
                ctr += 1
        if ctr % 3 == 1:
            ans = ans | ( 1 << bitind)
    return ans


def singleNumberII(nums):   #better
    nums.sort()
    n = len(nums)
    for i in range(1, n, 3):
        if nums[i] != nums[i - 1]:
            return nums[i - 1]
    return nums[n - 1]

def singleNumberII(nums):   #optimal
    ones = 0
    twos = 0
    for i in range(len(nums) - 1):
        ones = (ones ^ nums[i]) & ~twos
        twos = (twos ^ nums[i]) & ~ones
    return ones