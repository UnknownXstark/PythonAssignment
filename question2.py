#  Write a function that takes a number and returns its reverse without converting it to a string.

def reverseEngineering(num):
    reverse = 0
    while num != 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10
    return reverse
print(reverseEngineering(123))