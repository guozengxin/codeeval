#!/usr/bin/env python
# https://www.codeeval.com/open_challenges/21/

import sys


def solve(num):
    s = 0
    for c in num:
        s += int(c)
    print(s)


def main():
    f = sys.argv[1]
    with open(f, 'r') as fp:
        for line in fp:
            solve(line.strip())

if __name__ == '__main__':
    main()
