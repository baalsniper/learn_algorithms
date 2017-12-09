# -*- coding: utf-8 -*-
import time 
import math

def prime(n):
    if n == 1: return False
    for i in range(2, n):
        if n % i == 0: return False
    return True
    

def prime1(n):
    max_divisor = math.floor(math.sqrt(n))
    if n == 1: return False
    for i in range(2, 1+int(max_divisor)):
        if n % i == 0: return False
    return True

    
def prime2(n):
    max_divisor = math.floor(math.sqrt(n))
    if n == 1: return False
    if (n > 2 and n % 2 == 0) or (n > 3 and n % 3 == 0): return False
    for i in range(4,1+int(max_divisor)):
        if n % i == 0: return False
    return True

def prim3(n):# Eratosthenes
      
    danh_dau=[True]*(n+1) # giả sự lúc đầu đều có thể là snt
    
    can_n=int(n**0.5)+1 # = floor(sqrt(n))+1
    
    for i in range(2,can_n+1): # i= 2->can_n
        if danh_dau[i]: # i là số nguyên tố
            
            for j in range(i*i,n+1,i): # j=i*i, i*i+i , ...,n
                danh_dau[j]=False ## j khong là số nguyên tố
    
    for i in range(2,n+1): #i= 2->n
        if danh_dau[i]: print i

def atkin(limit):
    """
    :param limit: The upper limit in which to find all primes less than this
                  value.
    """
    if limit == 2:
        return [2]
    if limit == 3:
        return [2, 3]
    if limit == 5:
        return [2, 3, 5]
    if limit < 2:
        return []
    primes = [2, 3, 5]
    is_prime = [False] * (limit + 1)
    sqrt_limit = int(sqrt(limit)) + 1
 
    for x in range(1, sqrt_limit):
        for y in range(1, sqrt_limit):
            n = 4 * x ** 2 + y ** 2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                is_prime[n] = not is_prime[n]
            n = 3 * x ** 2 + y ** 2
            if n <= limit and (n % 12 == 7):
                is_prime[n] = not is_prime[n]
            n = 3 * x ** 2 - y ** 2
            if x > y and (n <= limit) and (n % 12 == 11):
                is_prime[n] = not is_prime[n]
 
    for index in range(5, sqrt_limit):
        if is_prime[index]:
            for composite in range(index ** 2, limit, index ** 2):
                is_prime[composite] = False
                
    for index in range(7, limit):
        if is_prime[index]:
            print index

if __name__ == "__main__":
    t0 = time.time()
    for x in range(2,100):
        y = prime2(x)
        if y == True:
            print x
    t1 = time.time()
    print ("Time required: ", t1-t0)