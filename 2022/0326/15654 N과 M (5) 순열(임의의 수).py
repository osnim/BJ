import sys

N, M = map(int, sys.stdin.readline().split())
numList = list(map(int, sys.stdin.readline().split()))
numList.sort()
s = []

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in numList:
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
dfs()