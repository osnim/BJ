#M : 상어 개수
#  r, c
#  s 속도
#  d 방향
#  z 크기

def fishing(man):
    global ans
    tempsharkInfo = []
    #가장 가까운거 먹음
    delCol = -1
    rmin = 101
    tempz = 0
    for i in range(len(sharkInfo)):
        r, c, s, d, z = sharkInfo[i]
        if c == man and r < rmin:
            rmin = r
            delCol = i
            tempz = z

    if delCol == -1:
        return

    sharkInfo.pop(delCol)
    ans += tempz


def rotate():
    global sharkInfo
    tempsharkInfo = []
    #d = [1, 2, 3, 4]  # 북 남 동 서
    delIdx = []
    sharkMAP = [[0] * (C+1) for _ in range(R+1)]
    for i in range(len(sharkInfo)):
        r, c, s, d, z = sharkInfo[i]
        nr, nc = r, c
        for _ in range(1, s+1):
            if d == 1: # 북
                nr -= 1
                if nr < 1:
                    d = 2
                    nr += 2
                    continue
            elif d == 2: # 남
                nr += 1
                if nr > R:
                    d = 1
                    nr -= 2
                    continue
            elif d == 3: # 동
                nc += 1
                if nc > C:
                    d = 4
                    nc -= 2
                    continue
            elif d == 4: # 서
                nc -= 1
                if nc < 1:
                    d = 3
                    nc += 2
                    continue

        r, c = nr, nc
        #칸이 비었을때만 임시 저장소에 저장
        if not sharkMAP[r][c]:
            tempsharkInfo.append([r, c, s, d, z])
            sharkMAP[r][c] = 1
    #while tempsharkInfo:
    #for i in range()

    sharkInfo = tempsharkInfo[:]
    return
R, C, M = map(int, input().split())
sharkInfo = []
# sharks = [[0]*C-1 for _ in range(R)]
# sharkMap = [[[0]*C for _ in range(R)] for i in range(M)]
ans = 0
for i in range(M):
    sharkInfo.append(list(map(int, input().split())))
    #r, c, s, d, z = map(int, input().split())
    #sharks[c] = [r, s, d, z]

#C 만큼 반복, 사람 이동, y좌표
man = 0
sharkInfo.sort(key=lambda x: (-x[4]))  # 크기가 가장 큰 상어부터 시작
for i in range(C):
    man += 1
    #sharkInfo.sort(key=lambda x: (x[0]))  # 가장 행이 낮은거 부터 시작
    #sharkInfo = fishing(man, sharkInfo)
    fishing(man)
    #sharkInfo.sort(key=lambda x: (-x[4]))  # 크기가 가장 큰 상어 부터 시작
    #sharkInfo = rotate(sharkInfo)
    rotate()

print(ans)



