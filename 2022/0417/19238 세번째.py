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
            result = (fuel - f) * 2 + f
            return result
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N or g[nx][ny] == -1:
                continue
            if g[nx][ny] == 0:
                g[nx][ny] = f-1
                q.append([nx, ny, f-1])

    print(-1)
    exit(0)
    return

def BFS(tx, ty, fuel):
    visited = [[0]*N for _ in range(N)]
    g = [i[:] for i in Cgraph]
    q = deque([])
    q.append([tx, ty, fuel])
    custList = [] # 같은 거리에 있는 손님들 리스트
    findCust = False
    minFuel = fuel
    if g[tx][ty] == -2:
        link = startLink[tx][ty]
        destX, destY = endLink[link]
        f = findDest(tx, ty, fuel, destX, destY)
        Cgraph[tx][ty] = 0
        return destX, destY, f
    while q:
        x, y, f = q.popleft()
        if f <= -1:
            print(-1)
            exit(0)
        #택시의 위치랑 손님의 위치랑 같을 떄
        #같은 거리에 있는 손님들 다 찾기 반례 : 왼왼왼 보다 오오위 가 더 우선

        visited[x][y] = 1
        g[x][y] = f
        for dx, dy in (-1, 0), (0, -1), (0, 1), (1, 0):  # 행 번호 > 열 번호 낮은 순서
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N or g[nx][ny] == -1:
                continue
            if g[nx][ny] == 0 and not visited[nx][ny]:
                g[nx][ny] = f - 1
                q.append([nx, ny, f - 1])

        # 같은 거리 손님 있는지 있으면 행 과 열 낮은 순 찾기
        if startLink[x][y] != 0 and findCust and minFuel == f:
            custList.append([x, y])

        if f < minFuel and findCust:
            custList.sort()
            link = startLink[custList[0][0]][custList[0][1]]
            destX, destY = endLink[link]
            startx, starty = custList[0][0], custList[0][1]
            f = findDest(startx, starty, minFuel, destX, destY)
            startLink[startx][starty] = 0
            return destX, destY, f

        # 가까운 손님 찾았다면
        if startLink[x][y] != 0 and not findCust:
            #minFuel = min(minFuel, f)
            minFuel = f
            findCust = True
            custList.append([x, y])
            #마지막 칸에 존재한다면
            if custList and not q:
                link = startLink[custList[0][0]][custList[0][1]]
                destX, destY = endLink[link]
                startx, starty = custList[0][0], custList[0][1]
                f = findDest(startx, starty, minFuel, destX, destY)
                startLink[startx][starty] = 0
                return destX, destY, f

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
startLink = [[0, 0] * N for i in range(N)]
endLink = [[] for i in range(M+1)]
for i in range(1, M+1):
    cx, cy, dx, dy = map(int, input().split())
    startLink[cx-1][cy-1] = i
    endLink[i] = [dx-1, dy-1]

#그냥 BFS로 손님 탐색
tx, ty = tx-1, ty - 1
for i in range(M):
    tx, ty, fuel = BFS(tx, ty, fuel)

print(fuel)
