import sys
N, M, H = map(int, sys.stdin.readline().split())
arr = [0]*(N+1)

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    arr[y] += 1
    arr[y+1] += 1

ans = 0
for i in range(1, N):
    if arr[i] % 2 == 1:
        arr[i] += 1
        arr[i+1] += 1
        ans += 1

for i in arr:
    if i >= H or (i%2 == 1):
        print(-1)
        exit(0)

if ans > 3:
    print(-1)
else:
    print(ans)