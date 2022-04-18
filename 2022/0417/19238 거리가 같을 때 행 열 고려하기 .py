from collections import deque
def findDest(x, y, fuel, destX, destY):
    g = [i[:] for i in wall]
    q = deque([])
    q.append([x, y, fuel])
    while q:
        x, y, f = q.popleft()
        g[x][y] = f
        if f <= -1:
            print(-1)
            exit(0)
        if x == destX and y == destY:
            #g[x][y] = f
            result = (fuel - f) * 2 + f
            return result
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N or g[nx][ny] == -1:
                continue
            if g[nx][ny] == 0:
                g[nx][ny] = f-1
                q.append([nx, ny, f-1])

def BFS(tx, ty, fuel):
    visited = [[0]*N for _ in range(N)]
    g = [i[:] for i in Cgraph]
    q = deque([])
    q.append([tx, ty, fuel])
    Find = False
    custList = [] # 같은 거리에 있는 손님들 리스트
    custDist = 0
    findCust = False
    minFuel = fuel
    if g[tx][ty] == -2:
        #custDist = f
        #custList.append([x, y, f])
        # if custDist == f:

        destX, destY = startEnd[tx][ty]
        # g[destX][destY] = findDest(x, y, f - 1, destX, destY)
        f = findDest(tx, ty, fuel, destX, destY)
        Cgraph[tx][ty] = 0
        # graph[destX][destY] = 0
        # g[nx][ny] = 0
        # Find = True
        # tx, ty =
        return destX, destY, f
    while q:
        x, y, f = q.popleft()
        if f <= -1:
            print(-1)
            exit(0)
        #택시의 위치랑 손님의 위치랑 같을 떄
        #같은 거리에 있는 손님들 다 찾기 반례 : 왼왼왼 보다 오오위 가 더 우선

        visited[x][y] = 1
        # 가까운 손님 찾았다면 다른 같은 거리 손님 있는지 있으면 행 과 열 낮은 순 찾기
        if startEnd[x][y] != 0:
            #minFuel = min(minFuel, f)
            minFuel = f
            custList.append([x, y])
            while q:
                tempx, tempy, f = q.popleft()
                visited[tempx][tempy] = 1
                if f < minFuel:
                    break
                if minFuel == f and startEnd[tempx][tempy] != 0 and not [tempx, tempy] in custList:
                    custList.append([tempx, tempy])
                for dx, dy in (-1, 0), (0, -1), (0, 1), (1, 0):  # 행 번호 > 열 번호 낮은 순서
                    nx, ny = tempx + dx, tempy + dy
                    if nx < 0 or nx >= N or ny < 0 or ny >= N or g[nx][ny] == -1:
                        continue
                    if g[nx][ny] == 0 and not visited[nx][ny]:
                        g[nx][ny] = f-1
                        q.append([nx, ny, f - 1])

            custList.sort()
            #destX, destY = startEnd[x][y]
            destX, destY = startEnd[custList[0][0]][custList[0][1]]
            f = findDest(x, y, minFuel, destX, destY)
            startEnd[x][y] = 0
            return destX, destY, f


        g[x][y] = f
        for dx, dy in (-1, 0), (0, -1), (0, 1), (1, 0): #행 번호 > 열 번호 낮은 순서
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N or g[nx][ny] == -1:
                continue
            if g[nx][ny] == 0 and not visited[nx][ny]:
                #g[nx][ny] = f-1
                q.append([nx, ny, f-1])


    print(-1)
    exit(0)

N, M, fuel = map(int, input().split())
# 손님 정보까지 있는 그래프
Cgraph = []

for i in range(N):
    temp = list(map(int, input().split()))
    if 1 in temp:
        for j in range(N):
            if temp[j] == 1:
                temp[j] = -1
    Cgraph.append(temp)

wall = [i[:] for i in Cgraph]

tx, ty = map(int, input().split())
#datas = []
#closetCstm = int(10e9)
startEnd = [[0, 0] *N for i in range(N)]
for i in range(M):
    cx, cy, dx, dy = map(int, input().split())
    #dis = abs(tx - cx) + abs(ty - cy)
    #datas.append([dis, cx-1, cy-1, dx-1, dy-1])
    #Cgraph[cx-1][cy-1] = -2
    #dic = {cx-1, cy-1: dx-1, dy-1}
    startEnd[cx-1][cy-1] = [dx-1, dy-1]

#datas.sort(key = lambda  x:(x[0], ))
#datas.sort()
#print(dic)

#그냥 BFS로 손님 탐색
tx, ty = tx-1, ty - 1
for i in range(M):
    tx, ty, fuel = BFS(tx, ty, fuel)

print(fuel)


