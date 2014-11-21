#!/usr/bin/env python
# encoding=utf8
# https://www.codeeval.com/open_challenges/13/

import sys


def main(argv):
    inFile = argv[0]
    fp = open(inFile, 'r')
    for line in fp:
        inStr, remove = line.split(', ')
        count = {}
        for c in remove.strip():
            count[c] = 1
        r = ''
        for c in inStr:
            if c not in count:
                r += c
        print r
    fp.close()

if __name__ == '__main__':
    main(sys.argv[1:])
