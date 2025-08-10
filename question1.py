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