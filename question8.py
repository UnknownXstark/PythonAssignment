# Write a function that returns the number of digits in a number, without converting it to a string.

def countDigits(num):
    num = abs(num)
    if num == 0:
        return 1
    count = 0
    while num > 0:
        num //= 10
        count +=  1
    return count

print(countDigits(10))