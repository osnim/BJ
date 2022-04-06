import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

MAX = int(-1e9)
MIN = int(1e9)

def dfs(depth, total, plus, minus, mul, div):
    global MAX, MIN
    if depth == N:
        MAX = max(total, MAX)
        MIN = min(total, MIN)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, mul, div)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, mul, div)
    if mul:
        dfs(depth + 1, total * num[depth], plus, minus, mul - 1, div)
    if div:
        dfs(depth + 1, int(total / num[depth]), plus, minus, mul, div - 1)

dfs(1, num[0], op[0], op[1], op[2], op[3])
print(MAX)
print(MIN)