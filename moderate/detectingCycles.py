#!/usr/bin/env python
# https://www.codeeval.com/open_challenges/5/

import sys


def detect(arr, p2, p1):
    for i in range(len(arr) - p1):
        if arr[p2 + i] != arr[p1 + i]:
            return False
    return True


def solve(arr):
    L = len(arr)
    table = {}
    for i in range(L):
        num = arr[i]
        if num not in table:
            table[num] = []
        table[num].append(i)
        if len(table[num]) >= 2:
            p1 = i
            for p2 in table[num][:-1]:
                if detect(arr, p2, p1):
                    print ' '.join(arr[p2:p1])
                    return


def main():
    f = sys.argv[1]
    with open(f, 'r') as fp:
        for line in fp:
            arr = line.strip().split(' ')
            solve(arr)

if __name__ == '__main__':
    main()
