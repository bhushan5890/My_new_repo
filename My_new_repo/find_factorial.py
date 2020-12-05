# Python code to find factorial of a given number


def find_factorial_rec(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    elif num >= 2:
        return(num * find_factorial_rec(num - 1))


def find_fact(num):
    result = 1
    if num == 0:
        return 1
    elif num == 1:
        return 1
    elif num >= 2:
        for i in range(1, num+1):
            result *= i
    return result


'''
number = 8
for i in range(1, number + 1):
    print(f'Factorial of {i} is {find_factorial_rec(i)}')
'''
number = 0
for i in range(0, number + 1):
    print(f'Factorial of {i} is {find_fact(i)}')
