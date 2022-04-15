import sys

N, M = map(int, sys.stdin.readline().split())
numList = list(map(int, sys.stdin.readline().split()))
numList.sort()
s = []

def dfs(i):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for j in range(i, N):
        if numList[j] not in s:
            s.append(numList[j])
            dfs(j+1)
            s.pop()
dfs(0)