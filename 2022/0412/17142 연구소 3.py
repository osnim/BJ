from itertools import combinations
from collections import deque

def BFS(selectVirus, tempG):
    global ans
    count = 0
    visited = [[0] * N for i in range(N)]
    q = deque([])
    activeVirus = deque([])
    for i in range(len(selectVirus)):
         virus = selectVirus[i]
         q.append([virus[0], virus[1]])
         activeVirus.append([virus[0], virus[1]])
         visited[virus[0]][virus[1]] = 1
         tempG[virus[0]][virus[1]] = 0

    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            if visited[nx][ny]: continue
            # 이미 다른 바이러스가 방문
            if (tempG[nx][ny] <= tempG[x][y]+1) and visited[nx][ny]: continue
            if (nx, ny) in activeVirus: continue
            # 비활성 바이러스가 있을 때 => 활성바이러스로
            if tempG[nx][ny] == -1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx, ny])
                tempG[nx][ny] = tempG[x][y] + 1
                continue

            if (-1 < tempG[nx][ny] < 1) and not visited[nx][ny]: #빈칸인 경우만
                tempG[nx][ny] = tempG[x][y]+1
                q.append([nx, ny])
                count = max(count, tempG[nx][ny])
                visited[nx][ny] = 1

    for i in range(len(selectVirus)):
        virus = selectVirus[i]
        tempG[virus[0]][virus[1]] = -1

    for i in tempG:
        if 0 in i:
            return -1

    return count

N, M = map(int, input().split())
virusList = []
graph = []
entireCheck = int(10e9)
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] == 2:
            virusList.append([i, j])
            graph[i][j] = -1

def combi(i):
    if len(tempcombi) == M :
        # 대입이 아닌 리스트 슬라이스로 값만 복사하기
        vCombi.append(tempcombi[:])
        return

    for j in range(i, len(virusList)):
        if virusList[j] not in tempcombi:
            tempcombi.append(virusList[j])
            combi(j+1)
            tempcombi.pop()

vCombi = []
tempcombi = []
combi(0)
v = list(combinations(virusList, M))
result = []
Empty = True  # 빈칸이 남아있는 경우

for selectVirus in vCombi:
    tempG = [i[:] for i in graph]
    ans = BFS(selectVirus, tempG)
    if ans >= 0:
        Empty = False
        entireCheck = min(ans, entireCheck)
    result.append(ans)

if not Empty:
    print(entireCheck)
else:
    print(-1)




