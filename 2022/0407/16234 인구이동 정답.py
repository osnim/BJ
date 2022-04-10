from collections import deque
def loop():
    update = False
    global day
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                result = BFS(i, j, visited)
                if len(result) > 1:  # 합쳐진 나라가 있다면
                    update = True
                    num = sum(graph[x][y] for x, y in result) // len(result)

                    for x, y in result:
                        graph[x][y] = num

    if not update:  # 수정된 나라가 없다면
        return False
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
            nx, ny = x + dx, y + dy
            # 한번 이동한 경우 리스트에서 합 찾기
            # 차이가 기준 안에 들어 가고 연합이 아닐때
            if 0 <= nx < N and 0 <= ny < N:
                # 연합이 아닐때
                if L <= abs(graph[x][y] - graph[nx][ny]) <= R and not visited[nx][ny]:
                    visited[nx][ny] = True
                    tempSum += graph[nx][ny]
                    cnt += 1
                    q.append([nx, ny])
                    updateQ.append([nx, ny])
    return updateQ

N, L, R = map(int, input().split())
graph = []
day = 0
UnionList = []
for i in range(N):
    graph.append(list(map(int, input().split())))

for _ in range(2000):
    updateCnt = 1  # 인구수 수정된 나라 수
    if not loop():
        break

print(day)

