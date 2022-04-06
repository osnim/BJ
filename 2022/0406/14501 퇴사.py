def dfs(startDate, period, pay):
    global ans
    if not check(startDate, period):
        return
    ans = max(ans, pay)
    for i in range(startDate+period, N+1):
        T, P = arr[i]
        dfs(i, T, pay+P)

def check(date, period):
    if date+period <= N+1:
        return True
    return False

N = int(input())
arr = [[]]
ans = 0
for i in range(1, N+1):
    arr.append(list(map(int, input().split())))

for i in range(1, N+1):
    T, P = arr[i]
    dfs(i, T, P)
print(ans)


