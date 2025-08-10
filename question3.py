# Write a function that takes a list of integers and returns a new list with all even numbers doubled and odd numbers removed.

def listCompression(nums):
    return [n * 2 for n in nums if n % 2 == 0]

print(listCompression([1,2,3,4,5,6,7,8,9,12,23,24,25,26]))