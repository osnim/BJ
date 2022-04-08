import sys
MAP = []
zeroPos = []
cnt = 0

def check3by3(zeroI, zeroJ, temp):
    # 3x3 확인
    if 0 <= zeroI % 9 < 3:
        if 0 <= zeroJ % 9 < 3:
            for i in range(3):
                for j in range(3):
                    if MAP[i][j] == temp:
                        return False
        elif 3 <= zeroJ % 9 < 6:
            for i in range(3):
                for j in range(3, 6):
                    if MAP[i][j] == temp:
                        return False
        else:
            for i in range(3):
                for j in range(6, 9):
                    if MAP[i][j] == temp:
                        return False

    elif 3 <= zeroI % 9 < 6:
        if 0 <= zeroJ % 9 < 3:
            for i in range(3, 6):
                for j in range(3):
                    if MAP[i][j] == temp:
                        return False

        elif 3 <= zeroJ % 9 < 6:
            for i in range(3, 6):
                for j in range(3, 6):
                    if MAP[i][j] == temp:
                        return False
        else:
            for i in range(3, 6):
                for j in range(6, 9):
                    if MAP[i][j] == temp:
                        return False

    else:
        if 0 <= zeroJ % 9 < 3:
            for i in range(6, 9):
                for j in range(3):
                    if MAP[i][j] == temp:
                        return False

        elif 3 <= zeroJ % 9 < 6:
            for i in range(6, 9):
                for j in range(3, 6):
                    if MAP[i][j] == temp:
                        return False
        else:
            for i in range(6, 9):
                for j in range(6, 9):
                    if MAP[i][j] == temp:
                        return False
    return True

def promising(zeroI, zeroJ, temp):
    #3x3안에 없을때
    if check3by3(zeroI, zeroJ, temp):
        if temp not in MAP[zeroI]:  # 같은 행에 없을 때,
            tempcnt = 0
            for i in range(9):
                if temp != MAP[i][zeroJ]:  # 같은 열에 없을때
                    tempcnt += 1
                else:
                    return False
            if tempcnt == 9:
                return True
        else:
            return False
    else:
        return False

for i in range(9):
    MAP.append(list(map(int, sys.stdin.readline().split())))

for i in range(9):
    for j in range(9):
        if MAP[i][j] == 0:
            zeroPos.append([i,j])

flag = False
def sudoku(cnt):
    #global cnt
    if cnt == len(zeroPos):
        # 모든 0을 다 채운경우
        return
    for i in range(1, 10):
        #MAP[zeroPos[cnt][0]][zeroPos[cnt][1]] = i
        if promising(zeroPos[cnt][0], zeroPos[cnt][1], i):
            #x, y = zeroPos[cnt][0], zeroPos[cnt][1]
            MAP[zeroPos[cnt][0]][zeroPos[cnt][1]] = i
            #x, y =
            #cnt += 1
            sudoku(cnt+1)
            #cnt -= 1
            MAP[zeroPos[cnt][0]][zeroPos[cnt][1]] = 0
            #if cnt == len(zeroPos):
                # 모든 0을 다 채운경우
               # return

sudoku(cnt)
for i in range(9):
    print(" ".join(map(str, MAP[i])))
    #print(MAP[i])


