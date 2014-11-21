#!/usr/bin/env python
# https://www.codeeval.com/open_challenges/8/

import sys


def main():
    f = sys.argv[1]
    with open(f, 'r') as fp:
        for line in fp:
            arr = line.strip().split(' ')
            print ' '.join(reversed(arr))

if __name__ == '__main__':
    main()
