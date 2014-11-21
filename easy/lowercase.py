#!/usr/bin/env python
# https://www.codeeval.com/open_challenges/20/

import sys


def main():
    for line in sys.stdin:
        line = line.strip()
        print line.lower()

if __name__ == '__main__':
    main()
