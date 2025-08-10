# Write a function that returns the number of steps it takes to reach 1 using the Collatz rules:
# - If n is even, divide by 2.
# - If n is odd, n = 3 * n + 1.

def collatzConjecture(num):
    if num % 2 == 0:
        return num / 2
    else:
        return 3 * num + 1
print(collatzConjecture(3))