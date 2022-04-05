import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

MAP = [list(input().strip()) for _ in range(N)]
check = [[0] * M for _ in range(N)]

#BFS 와 queue 사용
q = [(0, 0)]
check[0][0] = 1

while q:
    x, y = q.pop(0)

    # N인지 M인지 헷갈리는데 q에서 x는 N의 범위에 속함
    if x == N-1 and y == M-1:
        print(check[x][y])
        break

    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx, ny = x+dx, y+dy

        # nx는 N의 범위에 속함, ny는 M의 범위에 속함
        if 0 <= nx < N and 0 <= ny < M:
            if check[nx][ny] == 0 and MAP[nx][ny] == '1':
                check[nx][ny] = check[x][y] +1
                q.append((nx, ny))
