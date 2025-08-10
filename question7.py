# Write a function that checks if a number is a palindrome without converting it to a string.

def palindromeCheck(num):
    original = num
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10
    return reverse == original
print(palindromeCheck(101))