import sys
n, m = map(int, sys.stdin.readline().split())
cctv = []
office = []
rotate = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    office.append(list(map(int, sys.stdin.readline().split())))
    for j in range(m):
        if 0 < office[i][j] < 6:
            cctv.append([office[i][j], i, j])

def check(board, cctvSight, x, y):
    for i in cctvSight:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0:
                board[nx][ny] = 7

def dfs(depth, office):
    global min_value
    if depth == len(cctv):
        count = 0
        for i in range(n):
            count += office[i].count(0)
        min_value = min(min_value, count)
        return
    temp = [i[:] for i in office]
    cctv_num, x, y = cctv[depth]
    for i in rotate[cctv_num]:
        check(temp, i, x, y)
        dfs(depth+1, temp)
        temp = [i[:] for i in office]

min_value = int(1e9)
dfs(0, office)
print(min_value)