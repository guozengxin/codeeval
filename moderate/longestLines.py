#!/usr/bin/env python
# encoding=utf8
# https://www.codeeval.com/open_challenges/2/

import sys

import heapq


class MaxHeap(object):
    def __init__(self, x):
        self.heap = [e for e in x]
        heapq.heapify(self.heap)

    def push(self, value):
        heapq.heappush(self.heap, value)

    def pop(self):
        return heapq.heappop(self.heap)


def main(argv):
    inputFile = argv[0]
    fp = open(inputFile)
    N = None
    maxHeap = None
    for line in fp:
        line = line.strip()
        if N is None:
            N = int(line)
            maxHeap = MaxHeap([])
        else:
            maxHeap.push([-(len(line)), line])
    for i in range(N):
        print maxHeap.pop()[1]
    print
    fp.close()


if __name__ == '__main__':
    main(sys.argv[1:])
