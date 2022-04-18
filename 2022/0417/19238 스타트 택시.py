from collections import deque
def findDest(x, y, fuel, destX, destY):
    visited = [[0] * N for _ in range(N)]
    g = [i[:] for i in graph]
    q = deque([])
    q.append([x, y, fuel])
    while q:
        x, y, f = q.popleft()
        if f <= -1:
            print(-1)
            exit(0)
        if x == destX and y == destY:
            #g[x][y] = f
            result = (fuel - f) * 2 + f
            return result
        g[x][y] = f
        visited[x][y] = 1
        for dx, dy in (-1, 0), (0, -1), (0, 1), (1, 0):
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N or g[nx][ny] == -1:
                continue
            if g[nx][ny] == 0 and not visited[nx][ny]:
                g[nx][ny] = f-1
                q.append([nx, ny, f-1])

def BFS(tx, ty, fuel):
    visited = [[0]*N for _ in range(N)]
    g = [i[:] for i in graph]
    q = deque([])
    q.append([tx, ty, fuel])
    dis, cx, cy, destX, destY = datas.pop(0)
    Find = False
    while q:
        x, y, f = q.popleft()
        if f <= -1:
            print(-1)
            exit(0)

        #손님 위치 찾기
        if x == cx and y == cy:
            #destX, destY = datas[3], datas[4]
            #g[destX][destY] = findDest(x, y, f - 1, destX, destY)
            f = findDest(x, y, f, destX, destY)
            graph[x][y] = 0
            # graph[destX][destY] = 0
            # g[nx][ny] = 0
            # Find = True
            # tx, ty =
            return destX, destY, f

        g[x][y] = f
        visited[x][y] = 1
        for dx, dy in (-1, 0), (0, -1), (0, 1), (1, 0): #행 번호 > 열 번호 낮은 순서
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N or g[nx][ny] == -1:
                continue
            if g[nx][ny] == 0 and not visited[nx][ny]:
                g[nx][ny] = f-1
                q.append([nx, ny, f-1])
            if nx == cx and ny == cy:
            #if g[nx][ny] == -2:
                #destX, destY = startEnd[nx][ny]
                # g[destX][destY] = findDest(x, y, f - 1, destX, destY)
                #f = findDest(x, y, f, destX, destY)
                f = findDest(nx, ny, f-1, destX, destY)
                graph[nx][ny] = 0
                return destX, destY, f

    print(-1)
    exit(0)

N, M, fuel = map(int, input().split())
# 손님 정보까지 있는 그래프
graph = []

for i in range(N):
    temp = list(map(int, input().split()))
    if 1 in temp:
        for j in range(N):
            if temp[j] == 1:
                temp[j] = -1
    graph.append(temp)

wall = [i[:] for i in graph]

tx, ty = map(int, input().split())
datas = []
#closetCstm = int(10e9)
#startEnd = [[0, 0] *N for i in range(N)]
for i in range(M):
    cx, cy, dx, dy = map(int, input().split())
    dis = abs(tx - cx) + abs(ty - cy)
    datas.append([dis, cx-1, cy-1, dx-1, dy-1])
    #Cgraph[cx-1][cy-1] = -2
    #dic = {cx-1, cy-1: dx-1, dy-1}
   #startEnd[cx-1][cy-1] = [dx-1, dy-1]

#datas.sort(key = lambda  x:(x[0], ))

#print(dic)

#그냥 BFS로 손님 탐색
tx, ty = tx-1, ty - 1
for i in range(M):
    datas.sort(key = lambda x: (x[0], x[1], x[2]))
    tx, ty, fuel = BFS(tx, ty, fuel)
    # 최단 경로 찾기
    for j in range(len(datas)):
        dis, cx, cy, destX, destY = datas.pop()
        dis = abs(tx - cx) + abs(ty - cy)
        datas.append([dis, cx, cy, destX, destY])
print(fuel)


