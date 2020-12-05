# Python code to print Fibonacci Series
def print_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


limit = 200
for f in print_fibonacci():
    if f > limit:
        break
    print(f, end='\t')
