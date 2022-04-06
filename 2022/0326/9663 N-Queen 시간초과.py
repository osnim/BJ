import sys
N = int(sys.stdin.readline())
col = [0] * N
result = 0
#유망한지, 열, 행, 대각선, 판단
def promising(depth):
    for j in range(depth):
        if col[depth] == col[j] or abs(col[depth] - col[j]) == abs(depth - j):
            return False
    return True

def N_Queen(depth):
    global result
    if depth == N:
        result += 1
        return
    else:
        for j in range(N):
            # [i,j]에 퀸을 놓겠다.
            col[depth] = j
            if promising(depth):
                N_Queen(depth+1)
N_Queen(0)
print(result)