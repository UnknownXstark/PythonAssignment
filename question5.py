#  Write a function to find the second largest number in a list without using sorting.

def secondLargest(nums):
    largest = secondLargest = float('-inf')
    for n in nums:
        if n > largest:
            secondLargest = largest
            largest = n
        elif n > secondLargest and n!= largest:
            secondLargest = n
            return secondLargest if secondLargest != float('-inf') else None

print(secondLargest([5,5,5,5]))

print()