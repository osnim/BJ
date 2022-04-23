def dust(tempGraph, graph):
    for x in range(R):
        for y in range(C):
            if graph[x][y] >= 5:
                #가능한 4방향 다 찾기
                temp = []
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    nx, ny = x+dx, y + dy
                    if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != -1:
                        temp.append([graph[x][y]//5, nx, ny])
                #확산
                for q, tx, ty in temp:
                    tempGraph[tx][ty] += q
                    graph[x][y] -= q
    #한번에 합치기
    for i in range(R):
        for j in range(C):
            graph[i][j] += tempGraph[i][j]

def clean(machine):
    mx1, mx2 = machine[0], machine[1]

    #청소는 회전 반대로 하기
    graph[mx1-1][0] = 0
    for r in range(mx1-2, -1, -1):
        if graph[r][0] > 0:
            graph[r+1][0] = graph[r][0]
            graph[r][0] = 0
    for c in range(1, C):
        if graph[0][c] > 0:
            graph[0][c-1] = graph[0][c]
            graph[0][c] = 0
    for r in range(1, mx1+1):
        if graph[r][C-1] > 0:
            graph[r-1][C-1] = graph[r][C-1]
            graph[r][C-1] = 0
    for c in range(C-2, 0, -1):
        if graph[mx1][c] > 0:
            graph[mx1][c+1] = graph[mx1][c]
            graph[mx1][c] = 0

    #시계 방향
    graph[mx2 + 1][0] = 0
    for r in range(mx2+2, R):
        if graph[r][0] > 0:
            graph[r-1][0] = graph[r][0]
            graph[r][0] = 0
    for c in range(1, C):
        if graph[R-1][c] > 0:
            graph[R-1][c-1] = graph[R-1][c]
            graph[R-1][c] = 0
    for r in range(R-2, mx2-1, -1):
        if graph[r][C-1] > 0:
            graph[r+1][C-1] = graph[r][C-1]
            graph[r][C-1] = 0
    for c in range(C-2, 0, -1):
        if graph[mx2][c] > 0:
            graph[mx2][c+1] = graph[mx2][c]
            graph[mx2][c] = 0

    return

R, C, T = map(int, input().split())
graph = []
machine = []
ans = 0
for i in range(R):
    graph.append(list(map(int, input().split())))
    if -1 in graph[i]:
        machine.append(i)

for i in range(T):
    tempGraph = [[0]*C for _ in range(R)]
    dust(tempGraph, graph)
    clean(machine)

for i in range(R):
    for j in range(C):
        if graph[i][j] != -1:
            ans += graph[i][j]

print(ans)
