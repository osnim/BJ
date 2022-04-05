import sys
from collections import deque

N = int(sys.stdin.readline().rstrip()) # N x N
K = int(sys.stdin.readline().rstrip()) # 사과 개수

graph = [[0]*(N) for _ in range(N)]
Body = [] #뱀의 몸통 좌표

for i in range(K):
    x, y = map(int, sys.stdin.readline().split())

    graph[x-1][y-1] = 1

L = int(sys.stdin.readline().rstrip()) # 뱀의 방향 변환 횟수
turnings = []

#동, 남, 서, 북
dx = [0,1,0,-1]
dy = [1,0,-1,0]
directions = [0, 1, 2, 3]

for i in range(L):
    X, C = sys.stdin.readline().split()
    #if C == "D":
    turnings.append([int(X), C])

def turn_right(directions):
    directions += 1
    if directions > 3:
        directions = 0
    return directions

def turn_left(directions):
    directions -= 1
    if directions < 0:
        directions = 3
    return directions

#뱀의 위치를 2로 표현
graph[0][0] = 2
x, y = 0, 0
#동쪽을 바라봄
directions = 0
time = 0
Body.append([0, 0])

while True:
    time += 1
    nx = x + dx[directions]
    ny = y + dy[directions]

    # 맵 안에 있고 몸통과 안 부딪혔다면
    if nx >= 0 and nx < N and ny >= 0 and ny < N and graph[nx][ny] != 2:
        # 사과가 없다면
        if graph[nx][ny] == 0:
            graph[nx][ny] = 2
            Body.append([nx, ny])
            temp_x, temp_y = Body.pop(0)
            graph[temp_x][temp_y] = 0

        # 사과가 있다면
        elif graph[nx][ny] == 1:
            graph[nx][ny] = 2
            Body.append([nx, ny])

    # 벽이나 몸에 부딪힌 경우
    else:
        print(time)
        break

    # 다음 위치로 머리 이동
    x, y = nx, ny

    if turnings:
        if time == turnings[0][0]:
            if turnings[0][1] == "L":
                directions = turn_left(directions)

            elif turnings[0][1] == "D":
                directions = turn_right(directions)

            turnings.pop(0)
