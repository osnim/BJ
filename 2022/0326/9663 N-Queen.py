import sys
N = int(sys.stdin.readline())
col = [0] * N
result = 0
def promising(col, depth):
    for j in range(depth+1, N):
        if col[depth] == col[j] or abs(col[depth] - col[j]) == abs(depth - j):
            return False
    return True

def N_Queen(col, depth):
    global result
    if promising(col, depth):
        if depth == N:
            result += 1
        else:
            for j in range(N):
                #[depth,j]에 퀸을 놓겠다.
                col[depth] = j
                N_Queen(col, depth+1)

N_Queen(col, 0)
print(result)