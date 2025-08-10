#  Given a list of numbers from 1 to n with one number missing, find the missing number.

def missingNumber(nums):
    n = len(nums) + 1
    expectedSum = n * (n + 1)//2
    actualSum = sum(nums)
    return expectedSum - actualSum
print(missingNumber([13]))