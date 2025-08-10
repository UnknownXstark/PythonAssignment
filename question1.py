#  Write a function that takes an integer and returns:
#  -'Even and divisible by 3' if it's both even and divisible by 3,
#  - 'Even' if only even,
#  - 'Odd' if it's odd,- 'Zero' if it’

def digitClassifier(num):
    if num == 0:
        return "Zero"
    elif num % 2 == 0 and num % 3 == 0:
        return "Even and divisible by 3"
    elif num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print (digitClassifier(12))