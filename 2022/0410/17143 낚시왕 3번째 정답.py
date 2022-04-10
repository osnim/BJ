from collections import deque
def fishing(man):
    global ans
    for i in range(1, R+1):
        if sharksMap[i][man] != 0:
            s, d, z = sharksMap[i][man]
            ans += z
            sharksMap[i][man] = 0
            return

def rotate2(sharksMap):
    tempMap = [[0]*(C) for _ in range(R)]
    MAPcheck = [[0] * (C) for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if sharksMap[r][c]:
                s, d, z = sharksMap[r][c]
                nr, nc = r, c
                for k in range(s):
                    nr, nc = nr + dx[d], nc + dy[d]
                    if 0 <= nr < R and 0 <= nc < C:
                        continue
                    else:
                        nr, nc = nr - (dx[d]*2), nc - (dy[d]*2)
                        if d == 1: # 북
                            d = 2
                        elif d == 2: #남
                            d = 1
                        elif d == 3:  # 동
                            d = 4
                        elif d == 4:  # 서
                            d = 3

                if not tempMap[nr][nc]:
                    tempMap[nr][nc] = [s, d, z]
                else:
                    if tempMap[nr][nc][2] < z:
                        tempMap[nr][nc] = [s, d, z]
    return tempMap

R, C, M = map(int, input().split())
sharkInfo = []
sharksMap = [[0]*(C+1) for _ in range(R+1)]
# sharkMap = [[[0]*C for _ in range(R)] for i in range(M)]
ans = 0
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]
for i in range(M):
    #sharkInfo.append(list(map(int, input().split())))
    r, c, s, d, z = map(int, input().split())
    sharksMap[r-1][c-1]=[s, d, z]
    #sharkInfo.append([r, c, s, d, z])

#C 만큼 반복, 사람 이동, y좌표
man = 0
#sharkInfo.sort(key=lambda x: (-x[4]))  # 크기가 가장 큰 상어부터 시작
for j in range(C):
    for i in range(R):
        if sharksMap[i][j] != 0:
            s, d, z = sharksMap[i][j]
            ans += z
            sharksMap[i][j] = 0
            break

    sharksMap = rotate2(sharksMap)

print(ans)



