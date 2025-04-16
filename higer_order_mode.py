from collections import Counter

def find_mode(numbers):
    return max(Counter(numbers).items(), key=lambda x: x[1])[0]
