#!/usr/bin/env python
# https://www.codeeval.com/open_challenges/27/

import sys


def main():
    f = sys.argv[1]
    with open(f, 'r') as fp:
        for line in fp:
            s = bin(int(line.strip()))
            print(s[2:])

if __name__ == '__main__':
    main()
