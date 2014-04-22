#!/usr/bin/env python
# encoding=utf8
# https://www.codeeval.com/open_challenges/6/

import sys

dp = None


def process(s1, s2):
    len1, len2 = len(s1), len(s2)
    global dp
    dp = [[0 for col in range(len2 + 1)] for row in range(len1 + 1)]
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            elif dp[i][j - 1] > dp[i - 1][j]:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[len1][len2]


def printLcs(s1, s2):
    result = ''
    len1, len2 = len(s1), len(s2)
    while len1 > 0 and len2 > 0:
        if (s1[len1 - 1] == s2[len2 - 1]) and (dp[len1][len2] == dp[len1 - 1][len2 - 1] + 1):
            result = s1[len1 - 1] + result
            len2 -= 1
            len1 -= 1
        elif (s1[len1 - 1] != s2[len2 - 1]) and (dp[len1 - 1][len2] > dp[len1][len2 - 1]):
            len1 -= 1
        else:
            len2 -= 1
    print result


def main(argv):
    inFile = argv[0]
    fp = open(inFile, 'r')
    for line in fp:
        s1, s2 = line.strip().split(';')
        process(s1, s2)
        printLcs(s1, s2)
    fp.close()

if __name__ == '__main__':
    main(sys.argv[1:])
