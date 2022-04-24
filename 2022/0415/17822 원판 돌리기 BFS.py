from collections import deque
import copy
def BFS(i, j, visited):
    return

N, M, T = map(int, input().split())
arr = [deque([])]
temp =[]
total = 0
for i in range(1, N+1):
    arr.append(deque(list(map(int, input().split()))))
    total += sum(arr[i])
numCnt = N * M
for _ in range(T):
    x, d, k = map(int, input().split()) # x 배수, d 시계, 반시계, k 회전 수
    #for i in range(x, N+1, x):
    while x <= N:
        #시계 회전
        if d == 0:
            arr[x].rotate(k)
        else:
            arr[x].rotate(-k)
        x += x

    update = False
    #인접칸 확인
    #numCnt = N * M

    #temp = arr.copy()
    #visited = [[0] * (M) for i in range(N+1)]
    visited = []
    updateList = []
    for i in range(1, N+1):
        for j in range(M):
            if arr[i][j] == 0:
                continue
            if [i, j] not in visited:
                q = deque([])
                q.append([i, j])

                while q:
                    x, y = q.popleft()
                    visited.append([x, y])
                    if x == 1:
                        for dx, dy in (0, 1), (0, -1), (1, 0):
                            nx, ny = (x + dx), (y + dy) % M
                            if nx > N or nx < 1:
                                continue
                            if arr[x][y] == arr[nx][ny] and [nx, ny] not in visited:
                                q.append([nx, ny])
                                updateList.append([nx, ny])
                                updateList.append([x, y])
                                #temp[x][y] = 0 # * 표시
                                update = True

                    elif i == N:
                        for dx, dy in (0, 1), (0, -1), (-1, 0):
                            if nx > N or nx < 1:
                                continue
                            nx, ny = (x + dx), (y + dy) % M
                            if arr[x][y] == arr[nx][ny] and [nx, ny] not in visited:
                                q.append([nx, ny])
                                #temp[x][y] = 0  # * 표시
                                updateList.append([nx, ny])
                                updateList.append([x, y])
                                update = True

                    else:
                        for dx, dy in (0, 1), (0, -1), (-1, 0), (1, 0):
                            nx, ny = (x + dx), (y + dy) % M
                            if nx > N or nx < 1:
                                continue
                            if arr[x][y] == arr[nx][ny] and [nx, ny] not in visited:
                                q.append([nx, ny])
                                #temp[x][y] = 0  # * 표시
                                updateList.append([nx, ny])
                                updateList.append([x, y])
                                update = True
    if not update:
        for i in range(1, N + 1):
            for j in range(M):
                if arr[i][j] == 0:
                    continue
                else:
                    if arr[i][j] < (total / numCnt):
                        arr[i][j] += 1
                    elif arr[i][j] == (total / numCnt):
                        continue
                    else:
                        arr[i][j] -= 1

    for [x, y] in updateList:
        total -= (arr[x][y])
        arr[x][y] = 0
        numCnt -= 1



print(total)












