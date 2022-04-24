from collections import deque
import copy
N, M, T = map(int, input().split())
arr = [deque([])]
temp =[]
total = 0
for i in range(1, N+1):
    arr.append(deque(list(map(int, input().split()))))
    total += sum(arr[i])
numCnt = N * M
for _ in range(T):
    x, d, k = map(int, input().split()) # x 배수, d 시계, 반시계, k 회전 수
    #for i in range(x, N+1, x):
    while x <= N:
        #시계 회전
        if d == 0:
            arr[x].rotate(k)
        else:
            arr[x].rotate(-k)
        x += x

    update = False
    #인접칸 확인
    #numCnt = N * M

    temp = arr.copy()

    for i in range(1, N+1):
        for j in range(M):
            if arr[i][j] == arr[i][(j+1)%M] and (arr[i][j] != 0 and arr[i][(j+1)%M] != 0):
                total -= (temp[i][j]+temp[i][(j+1)%M])
                temp[i][j], temp[i][(j+1)%M] = 0, 0  # * 표시
                numCnt -= 2
                update = True
            if arr[i][j] == arr[i][j-1] and (arr[i][j] != 0 and arr[i][j-1] != 0):
                total -= (temp[i][j] + temp[i][j - 1])
                temp[i][j], temp[i][j-1] = 0, 0
                numCnt -= 2
                update = True
            if i == 1:
                if arr[i][j] == arr[i + 1][j] and (arr[i][j] != 0 and arr[i+1][j] != 0):
                    total -= (temp[i][j] + temp[i+1][j])
                    temp[i][j], temp[i + 1][j] = 0, 0
                    numCnt -= 2
                    update = True
            elif i == N:
                if arr[i][j] == arr[i - 1][j] and (arr[i][j] != 0 and arr[i-1][j] != 0):
                    total -= (temp[i][j] + temp[i - 1][j])
                    temp[i][j], temp[i - 1][j] = 0, 0
                    numCnt -= 2
                    update = True
            else:
                if arr[i][j] == arr[i + 1][j] and (arr[i][j] != 0 and arr[i+1][j] != 0):
                    total -= (temp[i][j] + temp[i + 1][j])
                    temp[i][j], temp[i + 1][j] = 0, 0
                    numCnt -= 2
                    update = True
                if arr[i][j] == arr[i - 1][j] and (arr[i][j] != 0 and arr[i-1][j] != 0) :
                    total -= (temp[i][j] + temp[i - 1][j])
                    temp[i][j], temp[i - 1][j] = 0, 0
                    numCnt -= 2
                    update = True
    if not update:
        for i in range(1, N+1):
            for j in range(M):
                if arr[i][j] == 0:
                    continue
                else:
                    if arr[i][j] < (total / numCnt):
                        arr[i][j] += 1
                    elif arr[i][j] == (total / numCnt):
                        continue
                    else:
                        arr[i][j] -= 1

    else:
        arr = temp.copy()

print(total)












