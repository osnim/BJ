n = int(input())

dp = [[0]*11 for i in range(n+1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(0, 10):

        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

sum = 0
for i in range(10):
    sum += dp[n][i]

print(sum % 1000000000)