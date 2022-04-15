N, K = map(int, input().split())
chess = []

#말의 좌표와 방향
hInfoes = [[] for _ in range(N)]

#말이 쌓인 순서대로 저장
hgraph = [[[] for i in range(N)] for _ in range(N)]

#위에 쌓인 말들을 저장
hSet = [[] for _ in range(N)]

d = [1,2,3,4] # 동 서 북 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


for i in range(N):
    chess.append(list(map(int, input().split())))
for i in range(K):
    x, y, d = map(int, input().split())
    hgraph[x-1][y-1].append(i)
    #horses.append(list(i, x, y, d))
    hInfoes[i] = [x-1, y-1, d-1]

ans = 0
for _ in range(1000):
    for i in range(K):
        x, y, d = hInfoes[i]
        nx, ny = x+dx[d] + y+dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        # 흰색 칸
        if chess[nx][ny] == 0:
            # 말이 있을 때
            if hgraph[nx][ny]:
                hgraph[nx][ny].append(i)
                #below = hgraph[x][y][0]
                #나와 내 위에 말 모두 이동
                for j in range(3, len(horses[i])):
                    upNum = horses[i][j]
                    horses[upNum][0], horses[upNum][1] = nx, ny
                    #horses[below].append(i)
                    hgraph[nx][ny].append(upNum)

            #말이 없을 때
            else:
                hgraph[nx][ny].append(i)

                for h in hSet[i]:


