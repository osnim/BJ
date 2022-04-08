import sys
MAP = []
zeroPos = []
cnt = 0
def check3by3(x, y, a):
    # 3x3 확인
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == MAP[nx + i][ny + j]:
                return False
    return True
def checkRow(x, a):
    for i in range(9):
        if a == MAP[x][i]:
            return False
    return True
def checkCol(y, a):
    for i in range(9):
        if a == MAP[i][y]:
            return False
    return True

for i in range(9):
    MAP.append(list(map(int, sys.stdin.readline().split())))

for i in range(9):
    for j in range(9):
        if MAP[i][j] == 0:
            zeroPos.append([i,j])

flag = False
def sudoku(cnt):
    if cnt == len(zeroPos):
        for i in range(9):
            print(" ".join(map(str, MAP[i])))
        exit(0)

    for i in range(1, 10):
        x, y = zeroPos[cnt][0], zeroPos[cnt][1]
        if checkRow(x, i) and checkCol(y, i) and check3by3(x, y, i):
            MAP[x][y] = i
            sudoku(cnt+1)
            MAP[x][y] = 0
sudoku(cnt)
for i in range(9):
    print(" ".join(map(str, MAP[i])))


