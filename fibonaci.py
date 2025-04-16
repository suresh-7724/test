def generate_fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Example usage
n = int(input("Enter how many Fibonacci numbers to generate: "))
for num in generate_fibonacci(n):
    print(num)
