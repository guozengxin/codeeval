#!/usr/bin/env python
# https://www.codeeval.com/open_challenges/16/

import sys


def solve(num):
    r = 0
    while num > 0:
        num &= (num - 1)
        r += 1
    print r


def main():
    f = sys.argv[1]
    with open(f, 'r') as fp:
        for line in fp:
            solve(int(line.strip()))

if __name__ == '__main__':
    main()
