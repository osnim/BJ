import sys

def addLine(arr, cnt):
    if cnt > 2:
        return False
    for i in range(1, H+1):
        for j in range(1, N):
            if arr[i][j-1] == 0 and arr[i][j] == 0 and arr[i][j+1] == 0 and arr[i][j+2] == 0:
                arr[i][j], arr[i][j+1] = 1, 1
                return True
    return False

def DFS(graph, cnt, startCol):
    global ans
    print(f"열:{startCol}, cnt:{cnt}", )
    if cnt > 3:
        return
    if startCol > N:
        ans = min(ans, cnt)
        return
    #x, y = 1, 1
    #x, y 는 현재 이동하는 애들
    tempGraph = [i[:] for i in graph]
    y = startCol
    for i in range(N):
        #for _ in range(1, H + 1):
        for x in range(1, H + 1):
            # 그냥 밑으로 내려가기
            if tempGraph[x][y] == 0:
                x, y = x + 1, y
            # 옆으로 한칸 이동
            else:
                if y + 1 <= N and tempGraph[x][y + 1] == 1:
                    x, y = x + 1, y + 1
                else:
                    x, y = x + 1, y - 1

        if y == startCol: # 맞으면 옆 세로선으로,

        else: #틀리면 이전 DFS부터 다시

            DFS(graph, cnt, startCol + 1)
            tempGraph = [i[:] for i in graph]

            if addLine(tempGraph, cnt):
                cnt += 1
                y = 1  # 처음 세로열 부터 다시
            else:
                return

N, M, H = map(int, sys.stdin.readline().split())
#arr = [0]*(N+1)
graph = [[0]*(N+2) for i in range(H+1)]
ans = int(1e9)
for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y], graph[x][y+1] = 1, 1 #가로선 이미 존재
    #arr[y] += 1
    #arr[y+1] += 1

DFS(graph, 0, 1)
print(ans)




