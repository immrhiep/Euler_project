# -*- coding: utf-8 -*-
'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

import math


def is_Prime(n):
    # Kiem tra n co phai la so nguyen to
    count = 0
    if n == 1 or n == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if not n % i:
                count += 1 # Tang 1 neu i la uoc cua n
        if not count: # Neu count khac 0 thi n la so nguyen to
            return True
        else:
            return False

number = 600851475143
primes = []
for i in range(1, int(math.sqrt(number))+ 1):
    if not number % i and is_Prime(i): # Kiem tra i co phai la uoc cua n khong dong thoi la so nguyen to
        primes.append(i)

print primes[-1]