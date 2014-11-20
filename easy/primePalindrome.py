#!/usr/bin/env python

from math import sqrt


def isPrime(num):
    for i in range(2, int(sqrt(num) + 1)):
        if num % i == 0 and num != i:
            return False
    return True


def isPalindrome(num):
    num = str(num)
    l = len(num)
    for i in range(l / 2):
        if num[i] != num[l - i - 1]:
            return False
    return True


def main():
    num = 1000
    while num > 1:
        if isPalindrome(num) and isPrime(num):
            print num
            break
        num -= 1

if __name__ == '__main__':
    main()
