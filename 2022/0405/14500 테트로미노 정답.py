def dfs(x, y, depth, total):
  global ans
  # 현재의 depth에서 남은 종이 합이 최댓값이더라도 현재 최대값보다 작다면 리턴
  # 시간 초과를 벗어나기 위해
  if ans >= total + MAX * (4 - depth):
    return
  # 4개를 모두 찾은 경우
  if depth == 4:
    ans = max(ans, total)
    return
  else:
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1) :
      nx = x + dx
      ny = y + dy
      if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
        #ㅗ 모양을 위해, 2개 칸을 선택하면 자기 자신을 시작점으로 dfs 호출
        if depth == 2:
          visited[nx][ny] = True
          dfs(x, y, depth + 1, total + arr[nx][ny])
          visited[nx][ny] = False
        visited[nx][ny] = True
        dfs(nx, ny, depth + 1, total + arr[nx][ny])
        visited[nx][ny] = False

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0
# 종이에서 가장 큰 값 => 나중에 백트래킹을 위해
MAX = max(map(max, arr))

for x in range(N):
   for y in range(M):
       visited[x][y] = True
       dfs(x, y, 1, arr[x][y])
       # 다른 dfs에서 방문을 하기 위해 변경
       visited[x][y] = False

print(ans)