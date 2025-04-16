def calculate(func,value):
    return func(value)

circumference = lambda r:2 *3.14*r

print(calculate(circumference, 5))