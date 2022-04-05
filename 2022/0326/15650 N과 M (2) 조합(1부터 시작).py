import sys
N, M = map(int, sys.stdin.readline().split())
s = []

def dfs(i):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for j in range(i, N+1):
        if j not in s:
            s.append(j)
            dfs(j)
            s.pop()
dfs(1)