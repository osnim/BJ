'''
4x4, 물고기 M 마리, 이동방향 1부터 8까지  ←, ↖, ↑, ↗, →, ↘, ↓, ↙
상어와 물고기 같은 칸 가능, 둘 이상의 물고기 같은 칸 가능

마법 한번 다음과 같은 작업 순서
1. 복제 마법 시전 (5번에서 물고기 복제)
2. 모든 물고기 한 칸 이동
상어가 있는 칸 X, 물고기 냄새가 있는 칸 X, 격자 범위 벗어난 칸 이동 불가
각 물고기는 자신이 가지고 있는 이동방향이 이동할 수 있는 칸을 향할 때 까지 45도 반시계 회전
없으면 이동 X, 방향 제자리 > 이외의 경우 이동
3.상어 연속 3칸 이동(상, 하 좌 우만 가능) 만약 3칸 이동했는데 벗어나면 그 방법은 불가능
이동중 중간에 물고기 모두 제거, 물고기 냄새를 남김
가능한 이동 방법 중 제외되는 물고기가 가장 많은 방법으로 이동
경우가 여러가지면 사전순으로 가장 앞서는 방법 사용

가장 앞서는 방법, 먼저, 방향을 정수로 변환,
상=1 좌=2 하=3 우=4
변환을 모두 마쳤으면, 수를 이어 붙여 정수로 하나 만든다.

두 방법 A와 B가 있고, 각각을 정수로 변환한 값을 a와 b라고 하자.
a < b를 만족하면 A가 B보다 사전 순으로 앞선 것이다.

예를 들어, [상, 하, 좌]를 정수로 변환하면 132가 되고, [하, 우, 하]를 변환하면 343이 된다.
132 < 343이기 때문에, [상, 하, 좌]가 [하, 우, 하]보다 사전 순으로 앞선다.
총 43 = 64가지 방법을 사전 순으로 나열해보면
[상, 상, 상], [상, 상, 좌], [상, 상, 하], [상, 상, 우], [상, 좌, 상],
[상, 좌, 좌], [상, 좌, 하], [상, 좌, 우], [상, 하, 상], ...,
[우, 하, 하], [우, 하, 우], [우, 우, 상], [우, 우, 좌], [우, 우, 하], [우, 우, 우] 이다.

4. 두 번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라진다.
5. 1에서 사용한 복제완료, 모든 복제된 물고기는 1에서의 위치와 방향을 그대로 갖게 된다.

M, 물고기 수,
S 연습한 수

sx, sy
S번의 연습을 마친 후 격자에 있는 물고기의 수를 출력한다.
'''
def combi(i, temp):
    global combis
    if len(temp) == 3:
        combis.append(temp[:])
        return

    for j in range(1, 5):
        temp.append(j)
        combi(j, temp)
        temp.pop()
    return
#def goShark(sx, sy, d, cnt, tempEat, tempArr, dirList):
#DFS(sx, sy, 0, 0, [], arr)
def DFS(sx, sy, tempEatCnt, dirList, MAP):
    global maxEatCnt
    global ans
    if len(dirList) == 3:
        temp = (dirList[0] + 1) * 100 + (dirList[1] + 1) * 10 + dirList[2] + 1
        if maxEatCnt < tempEatCnt:
            maxEatCnt = tempEatCnt
            ans = temp
        elif maxEatCnt == tempEatCnt:
            ans = min(ans, temp)
        return

    #4방향 가야함
    #for dd in range(d, 4):
    tempArr = [i[:] for i in MAP]
    for d in range(4):
        nx, ny = sx + sdx[d], sy + sdy[d]
        #dirList.append(d)
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            continue
        #if pruning(nx, ny, dirList, tempEatCnt):
        if len(tempArr[nx][ny]) > 0:
            tempEatCnt += len(tempArr[nx][ny])
            # maxEatCnt = max(maxEatCnt, tempEatCnt)
            tempArr[nx][ny] = []
            # smell[nx][ny] = -2

        dirList.append(d)
        DFS(nx, ny, tempEatCnt, dirList, tempArr)
        tempArr = [i[:] for i in MAP]
        tempEatCnt -= len(tempArr[nx][ny])
        dirList.pop()


M, S = map(int, input().split())
#     ←, ↖,   ↑,  ↗, →, ↘, ↓, ↙
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
sdx = [-1, 0, 1, 0]
sdy = [0, -1, 0, 1]
smell = [[0]*4 for i in range(4)]
arr = [[[] for i in range(4)] for _ in range(4)]

for _ in range(M):
    x, y, d = map(int, input().split())
    arr[x-1][y-1].append(d)

sx, sy = map(int, input().split())
sx, sy = sx -1 , sy -1

# 방향 조합 3개 찾음
combis = []
#combi(1, [])
#print(combis)

# 물고기 한 칸 이동
for _ in range(S):
    ans = 999
    maxEatCnt = 0
    pastArr = [i[:] for i in arr]
    tempArr = [[[] for i in range(4)] for _ in range(4)]
    #물고기 이동
    for i in range(4):
        for j in range(4):
            if len(arr[i][j]) > 0:
                for d in arr[i][j]:
                    d = d-1
                    for _ in range(8):
                        move = False
                        nx, ny = i + dx[d], j + dy[d]
                        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or (nx == sx and ny == sy):
                            d = (d - 1 + 8) % 8
                            continue
                        # 물고기 냄새 있는 칸
                        if smell[nx][ny] < 0:
                            d = (d - 1 + 8) % 8
                            continue
                        else:
                            tempArr[nx][ny].append(d+1)
                            move = True
                            break
                    if not move:
                        tempArr[i][j].append(d + 1)

    arr = [i[:] for i in tempArr]

    # 상어 연속 3칸 이동
    DFS(sx, sy, 0, [], arr)
    if ans == 999:
        ans = 111

    # 두 번 전 연습에서 생긴 물고기의 냄새 1 제거.
    # 물고기에만 영향 미치니 나중에 더함
    for i in range(4):
        for j in range(4):
            if smell[i][j] < 0:
                smell[i][j] += 1

    dirList = [ans//100, (ans%100)//10, ans%10]
    nx, ny = sx, sy
    for d in dirList:
        nx, ny = nx + sdx[d-1], ny + sdy[d-1]
        if len(arr[nx][ny]) > 0:
            smell[nx][ny] = -2
        arr[nx][ny] = []
    sx, sy = nx, ny

    # 물고기 복사
    for i in range(4):
        for j in range(4):
            if len(pastArr[i][j]) > 0:
                for num in pastArr[i][j]:
                    arr[i][j].append(num)
fishCnt = 0
for i in range(4):
    for j in range(4):
        fishCnt += len(arr[i][j])

print(fishCnt)


