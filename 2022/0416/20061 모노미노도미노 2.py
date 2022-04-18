def clean(x):
    for i in range(4):
        graph[i][x] = 0

    return

def move(mono, t):
    for x, y in mono:
        nx, ny = x, y
        while True:
            if graph[nx][ny] == 0:
                ny += 1
                continue
            else:
                break
        graph[nx][ny] = 1

        # 행 증가
        nx, ny = x, y
        while True:
            if graph[nx][ny] == 0:
                nx += 1
                continue
            else:
                break




    return

N = int(input())
graph = [[0]*10 for i in range(10)]
mono = [[],[0,0],[0,0,0,1],[0,0,1,0]]
cnt = 0


for i in range(N):
    t, x, y = map(int, input().split())
    if t == 1:
        # 열 증가
        nx, ny = x, y
        #mono = [x, y]
        #move(mono, 1)
        while True:
            if graph[nx][ny] == 0:
                ny += 1
                continue
            else:
                break
        graph[nx][ny] = 1
        # 행 증가
        nx, ny = x, y
        while True:
            if graph[nx][ny] == 0:
                nx += 1
                continue
            else:
                break
        graph[nx][ny] = 1

    elif t == 2:
        mono = [[x, y], [x, y+1]]
        nx, ny = x, y
        #열 증가
        while True:
            if graph[nx][ny] == 0:
                ny += 1
                continue
            else:
                break
        graph[nx][ny] = 1
        graph[nx][ny-1] = 1
        #행 증가
        ny1, ny2 = y, y+1
        # 열 증가
        while True:
            if graph[x][ny] == 0:
                nx += 1
                continue
            else:
                break
        graph[nx][ny] = 1
        graph[nx][ny] = 1
    else:

           #연한 칸
        if y == 4:
            clean(10)
            cnt += 1

        elif y == 5:

        #6~9행 또는 열 확인
        else:

