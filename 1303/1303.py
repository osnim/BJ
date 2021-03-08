import sys
from collections import deque

def BFS():
    q.append((i, j))
    check[i][j] = 1
    count = 1

    while q:
        x, y = q.popleft()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x+dx, y+dy
            if 0 <= nx < M and 0 <= ny < N:
                if MAP[nx][ny] == MAP[x][y] and check[nx][ny] == 0:
                    check[nx][ny] = 1
                    q.append((nx, ny))
                    count += 1

    return count

N, M = map(int, sys.stdin.readline().split())

MAP = [list(input().strip()) for _ in range(M)]
check = [[0] * N for _ in range(M)]

q = deque()
WHITE_POWER, BLUE_POWER = 0, 0

#여기서 인덱스 에러남!! 열이 N이고 행이 M인데 N과 M을 순서대로 입력해서 계속 에러 발생
for i in range(M):
    for j in range(N):
        if check[i][j] == 0:
            temp = BFS()

            #우리팀
            if MAP[i][j] == 'W':
                WHITE_POWER += temp ** 2

            #적팀
            else:
                BLUE_POWER += temp ** 2

print(WHITE_POWER, BLUE_POWER)