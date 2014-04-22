#!/usr/bin/env python
# encoding=utf8
# https://www.codeeval.com/open_challenges/7/

import sys

def compute(flag, num1, num2):
    if flag == '+':
        return num1 + num2
    elif flag == '*':
        return num1 * num2
    elif flag == '/':
        return float(num1) / num2

def process(arr):
    flag = []
    result = None
    for c in arr:
        if c in ['+', '*', '/']:
            flag.append(c)
        else:
            num = int(c)
            if result == None:
                result = num
            else:
                needFlag = flag.pop()
                result = (compute(needFlag, result, num))
    print int(result)

def main(argv):
    inFile = argv[0]
    fp = open(inFile, 'r')
    for line in fp:
        arr = line.strip().split()
        process(arr)
    fp.close()

if __name__ == '__main__':
    main(sys.argv[1:])
