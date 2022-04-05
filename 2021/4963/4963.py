def dfs(x, y, graph): # dfs로 특정 노드를 방문하고 연결된 모든 노드들도 방문

    if x <= -1 or x >= w or y <= -1 or y >= h : #주어진 범위를 벗어나는 경우에는 즉시 종료
        return False

    if graph[x][y] == 0:
        return False

        graph[x][y] = 0 #방문한 곳은 0으로 표시

        #인접한 상하좌우, 대각선의 위치들도 모두 재귀적으로 호출

        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

        dfs(x - 1, y - 1)
        dfs(x + 1, y - 1)
        dfs(x + 1, y + 1)
        dfs(x - 1, y + 1)

        return True

    return False

w, h = map(int, input().split()) #w, h을 공백을 기준으로 구분하여 입력 받기

#2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(h):
    graph.append(list(map(int, input().split())))

result = 0
for i in range(h):
    for j in range(w):
    # 현재 위치에서 DFS 수행
        if graph[i][j] == 1:
            if dfs(j, i, graph) == True:
                result += 1

print(result)