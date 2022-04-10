from collections import deque

def loop():
    global day, updateCnt
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                result = BFS(i, j, visited)
                if result > 1: #합쳐진 나라가 있다면
                    num = sum(graph[x][y] for x, y in result)//len(result)

                    for x, y in result:

                    unionList.append(result)

    if updateCnt == 1: # 수정된 나라가 없다면
        #print(day)
        return False
        #exit(0)
    day += 1
    return True

def BFS(i, j, visited):
    global updateCnt
    q = deque([])
    q.append([i, j])

    updateQ = deque([])
    updateQ.append([i, j])
    tempSum = graph[i][j]
    cnt = 1
    visited[i][j] = True

    while q:
       x, y = q.popleft()
       for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
           nx, ny = x+dx, y+dy
           # 한번 이동한 경우 리스트에서 합 찾기
           # 차이가 기준 안에 들어 가고 연합이 아닐때
           if  0 <= nx < N and 0 <= ny < N:
               # 연합이 아닐때
               #if L <= abs(graph[x][y] - graph[nx][ny]) <= R and unionCheck[nx][ny] != unionCheck[x][y]:
               #if L <= abs(graph[x][y] - graph[nx][ny]) <= R and not visited[nx][ny]:
               #if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                   # 연합
                   #unionCheck[nx][ny] = unionCheck[x][y]
                   visited[nx][ny] = True
                   tempSum += graph[nx][ny]
                   cnt += 1
                   q.append([nx, ny])
                   updateQ.append([nx, ny])

    #update가 없는 경우
    if len(updateQ) == 1:
        #UnionList.append([i,j])
        return False
    else:
        newPopulation = tempSum // cnt
        UnionList.append(updateQ)
        while updateQ:
            x, y = updateQ.popleft()
            unionCheck[x][y] = unionCheck[i][j]
            #graph[x][y] = newPopulation
            updateCnt = max(cnt, updateCnt)
        return UnionList

N, L, R = map(int, input().split())
graph = []
cnt = 1
unionCheck = [[0] * N for _ in range(N)] # 연합을 구분 하기 위한 그래프
day = 0
UnionList = []
#updateCnt = 0 # 인구수 수정된 나라 수
for i in range(N):
    graph.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        unionCheck[i][j] = cnt
        cnt += 1

for _ in range(2000):
    updateCnt = 1  # 인구수 수정된 나라 수
    unionList = []
    if not loop():
        break



print(day)

