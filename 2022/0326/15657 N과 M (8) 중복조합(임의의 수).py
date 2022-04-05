import sys
N, M = map(int, sys.stdin.readline().split())
numList = list(map(int, sys.stdin.readline().split()))
numList.sort()
s = []

def dfs(i):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for j in range(0, N):
        if numList[i] <= numList[j]:
            s.append(numList[j])
            dfs(j)
            s.pop()
dfs(0)