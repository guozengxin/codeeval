#!/usr/bin/env python
# https://www.codeeval.com/open_challenges/10/

import sys


def solve(arr):
    index = int(arr[-1])
    arr = arr[:-1]
    if index <= len(arr):
        print arr[-index]


def main():
    f = sys.argv[1]
    with open(f, 'r') as fp:
        for line in fp:
            arr = line.strip().split(' ')
            solve(arr)

if __name__ == '__main__':
    main()
