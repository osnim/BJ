N = int(input())
days = [0]
salary = [0]
dp = [0]
for i in range(N):
    T, P = map(int, input().split())
    days.append(T)
    salary.append(P)
    dp.append(P)
dp.append(0)

for i in range(N, 0, -1):
    if days[i]+i <= N+1: #6일에 2일 짜리 상담 있으면 6, 7로 가능해서 <=과 N+1로 함
        dp[i] = max(dp[i+1], dp[i]+dp[i+days[i]])
    else:
        dp[i] = dp[i+1]

print(dp[1])
