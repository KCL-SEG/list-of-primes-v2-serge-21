"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import math

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("number must be greater than 0")
    list = []
    i = 0
    while i < len(list):
        if isPrime(i):
            list.append(i)
        i += 1
    return list

def isPrime(number):
    if number <= 1:
        return False

    upperBound = int(math.ceil(math.sqrt(number)))
    for i in range(2, upperBound):
        if number % i == 0:
            return False
    return True