from collections import deque
def fishing(man):
    global ans
    for i in range(1, R+1):
        if len(sharksMap[i][man]) > 0:
            s, d, z = sharksMap[i][man].pop()
            ans += z
            return


def rotate2(sharksMap):
    tempMap = [[deque() for _ in range(C + 1)] for _ in range(R + 1)]
    MAPcheck = [[0] * (C + 1) for _ in range(R + 1)]

    for r in range(1, R+1):
        for c in range(1, C+1):
            if sharksMap[r][c]:
                s, d, z = sharksMap[r][c].popleft()
                nr, nc = r, c
                for _ in range(1, s + 1):
                    if d == 1:  # 북
                        nr -= 1
                        if nr < 1:
                            d = 2
                            nr += 2
                            continue
                    elif d == 2:  # 남
                        nr += 1
                        if nr > R:
                            d = 1
                            nr -= 2
                            continue
                    elif d == 3:  # 동
                        nc += 1
                        if nc > C:
                            d = 4
                            nc -= 2
                            continue
                    elif d == 4:  # 서
                        nc -= 1
                        if nc < 1:
                            d = 3
                            nc += 2
                            continue
                if not tempMap[nr][nc]:
                    #tempsharkInfo.append([nr, nc, s, d, z])
                    MAPcheck[nr-1][nc-1] = 1
                    tempMap[nr][nc].append([s, d, z])

    return tempMap

R, C, M = map(int, input().split())
sharkInfo = []
sharksMap = [[deque() for _ in range(C+1)] for _ in range(R+1)]
# sharkMap = [[[0]*C for _ in range(R)] for i in range(M)]
ans = 0
for i in range(M):
    #sharkInfo.append(list(map(int, input().split())))
    r, c, s, d, z = map(int, input().split())
    sharksMap[r][c].append([s, d, z])
    #sharkInfo.append([r, c, s, d, z])


#C 만큼 반복, 사람 이동, y좌표
man = 0
#sharkInfo.sort(key=lambda x: (-x[4]))  # 크기가 가장 큰 상어부터 시작
for i in range(C):
    man += 1
    fishing(man)
    sharksMap = rotate2(sharksMap)

print(ans)



