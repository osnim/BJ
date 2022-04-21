import sys
from collections import deque
# 구슬 굴리기 가능한지 판단
def moveCheck(x, y, dx, dy):
    cnt = 0
    while MAP[x+dx][y+dy] != "#":
        if MAP[x+ dx][y+ dy] == "O":
            return -1, -1, cnt
        x, y = x + dx, y + dy
        cnt += 1
    return x, y, cnt

def BFS(MAP, rx, ry, bx, by, cnt):
    redQ = deque([[rx, ry]])
    blueQ = deque([[bx, by]])
    visited = {}
    visited[rx, ry, bx, by] = cnt

    while redQ and blueQ:
        rx, ry = redQ.popleft()
        bx, by = blueQ.popleft()
        for i in range(4):
            nrx, nry, rcnt = moveCheck(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = moveCheck(bx, by, dx[i], dy[i])
            # 파란공 또는 빨간공, 파란공 동시에 탈출 하는 경우
            if nbx == -1 and nby == -1:
                continue
            # 빨간공만 탈출하는 경우
            elif nrx == -1 and nry == -1:
                return visited[rx, ry, bx, by]+1
            #두 공의 위치가 같은 경우, 덜 이동한게 뒤에 있다.
            elif nrx == nbx and nry == nby:
                if bcnt > rcnt:
                    bcnt -= 1
                    nbx, nby = nbx-dx[i], nby-dy[i]
                else:
                    rcnt -= 1
                    nrx, nry = nrx - dx[i], nry - dy[i]
            #전에 방문 했는지 안했는지 체크
            if (nrx, nry, nbx, nby) not in visited:
                visited[nrx, nry, nbx, nby] = visited[rx, ry, bx, by] + 1
                redQ.append([nrx, nry])
                blueQ.append([nbx, nby])

        if not (redQ and blueQ) or visited[rx, ry, bx, by] >= 10:
            return -1

N, M = map(int, sys.stdin.readline().split())
MAP = []
for i in range(N):
    MAP.append(list(sys.stdin.readline().rstrip()))

rx, ry, bx, by, ox, oy = 0, 0, 0, 0, 0, 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 'R':
            rx, ry = i, j
        if MAP[i][j] == 'B':
            bx, by = i, j
        if MAP[i][j] == 'O':
            ox, oy = i, j

print(BFS(MAP, rx, ry, bx, by, 0))

