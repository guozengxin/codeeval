#!/usr/bin/env python
# encoding=utf8

import sys


class Stack():
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def empty(self):
        return self.items.size() == 0


def process(arr):
    stack = Stack()
    for a in arr:
        stack.push(a)

    result = []
    while True:
        n = stack.pop()
        if not n:
            break
        result.append(n)
        n = stack.pop()
    print ' '.join(result)


def main(argv):
    inFile = argv[0]
    fp = open(inFile, 'r')
    for line in fp:
        arr = line.strip().split()
        process(arr)
    fp.close()


if __name__ == '__main__':
    main(sys.argv[1:])
