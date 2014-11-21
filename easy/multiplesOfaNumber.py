#!/usr/bin/env python

import sys


def solve(x, n):
    i = 1
    while True:
        m = n * i
        if m >= x:
            print m
            break
        i += 1


def main():
    f = sys.argv[1]
    with open(f, 'r') as fp:
        for line in fp:
            arr = line.strip().split(',')
            solve(int(arr[0]), int(arr[1]))

if __name__ == '__main__':
    main()
