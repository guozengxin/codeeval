#!/usr/bin/env python
# encoding=utf8
# https://www.codeeval.com/open_challenges/19/

import sys


def process(line):
    arr = line.split(',')
    n, p1, p2 = int(arr[0]), int(arr[1]), int(arr[2])
    num1 = 1 << (p1 - 1)
    num2 = 1 << (p2 - 1)
    if ((n & num1) >> (p1 - 1)) == ((n & num2) >> (p2 - 1)):
        print 'true'
    else:
        print 'false'


def main(argv):
    if len(argv) < 1:
        sys.exit(1)
    inputFile = argv[0]
    fp = open(inputFile, 'r')
    for line in fp:
        process(line.strip())


if __name__ == '__main__':
    main(sys.argv[1:])
