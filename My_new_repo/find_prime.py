# Python code for finding the  prime numbers upto the limit

import math


def is_prime(limit):
    if limit <= 1:
        return False
    elif limit == 2:
        return True
    elif limit > 2 and limit % 2 == 0:
        return False
    else:
        max_div = math.floor(math.sqrt(limit))

        for i in range(3, max_div + 1, 2):
            if limit % i == 0:
                return False
        return True


'''
print("is_prime(1)",is_prime(1))
print("is_prime(2)",is_prime(2))
print("is_prime(25)",is_prime(25))    
print("is_prime(101)",is_prime(101))
'''
num = 1000
for i in range(1, num+1):
    if is_prime(i) == True:
        print(i, end='\t')
