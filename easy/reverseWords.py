#!/usr/bin/env python

import sys


def main():
    f = sys.argv[1]
    with open(f, 'r') as fp:
        for line in fp:
            arr = line.strip().split(' ')
            print ' '.join(reversed(arr))

if __name__ == '__main__':
    main()
