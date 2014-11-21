#!/usr/bin/env python
# encoding=utf8
# https://www.codeeval.com/open_challenges/12/

import sys


def main(argv):
    inFile = argv[0]
    fp = open(inFile, 'r')
    for line in fp:
        line = line.strip()
        count = {}
        for c in line:
            if c not in count:
                count[c] = 0
            count[c] += 1
        for c in line:
            if count[c] == 1:
                print c
                break
    fp.close()

if __name__ == '__main__':
    main(sys.argv[1:])
