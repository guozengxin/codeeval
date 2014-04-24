#!/usr/bin/env python
# encoding=utf8
# https://www.codeeval.com/open_challenges/14/

import sys
import math


def perm(arr):
    arr = sorted(arr)
    length = len(arr) - 1
    all = math.factorial(length + 1)
    index = length
    sys.stdout.write(''.join(arr) + ',')
    now = 1
    while index > 0:
        pre = index
        index -= 1
        if arr[index] < arr[pre]:
            pMax = length
            while arr[pMax] <= arr[index]:
                pMax -= 1
            arr[index], arr[pMax] = arr[pMax], arr[index]
            arr[pre:] = arr[pre:][::-1]
            now += 1
            if now != all:
                sys.stdout.write(''.join(arr) + ',')
            else:
                sys.stdout.write(''.join(arr))
            index = length
        if index == 0:
            break
    print


def main(argv):
    inFile = argv[0]
    fp = open(inFile, 'r')
    for line in fp:
        perm(list(line.strip()))
    fp.close()

if __name__ == '__main__':
    main(sys.argv[1:])
