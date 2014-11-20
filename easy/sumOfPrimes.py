#!/usr/bin/env python

from math import sqrt


def isPrime(num):
    for i in range(2, int(sqrt(num) + 1)):
        if num % i == 0 and num != i:
            return False
    return True


def main():
    num = 2
    i = 0
    result = 0
    while True:
        if isPrime(num):
            result += num
            i += 1
        if i >= 1000:
            break
        num += 1
    print result


if __name__ == '__main__':
    main()
