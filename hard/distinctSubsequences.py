#!/usr/bin/env python

import sys


def solve(X, Z):
    lX = len(X)
    lZ = len(Z)
    dp = [[0] * (lX + 1) for i in range(lZ + 1)]
    dp[0][0] = 1
    for i in range(1, lX + 1):
        dp[0][i] = 1
    for i in range(1, lZ + 1):
        dp[i][0] = 0
    for i in range(1, lZ + 1):
        for j in range(1, lX + 1):
            dp[i][j] = dp[i][j - 1]
            if Z[i - 1] == X[j - 1]:
                dp[i][j] += dp[i - 1][j - 1]
    return dp[lZ][lX]


def main():
    for line in sys.stdin:
        (X, Z) = line.strip().split(',')
        print solve(X, Z)

if __name__ == '__main__':
    main()
