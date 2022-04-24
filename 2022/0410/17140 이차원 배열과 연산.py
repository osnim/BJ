from collections import deque
r, c, k = map(int, input().split())
arr = []
r, c= r-1, c-1
ans = 0
for i in range(3):
    arr.append(list(map(int, input().split())))
while True:
    if arr[r][c] == k:
       print(ans)
       break
    if ans > 100:
        print(-1)
        break
    ans += 1

#R 연산
    if rlen >= clen:
        maxLen = -1
        for i in range(rlen):
            checkList = []
            for j in range(clen):
                num = arr[i][j]
                if num > 0:
                    if [num, arr[i].count(num)] not in checkList:
                        checkList.append([num, arr[i].count(num)])

            checkList.sort(key=lambda x: (x[1], x[0]))
            arr[i] = sum(checkList, [])
            maxLen = max(maxLen, len(arr[i]))

        # 0으로 채우기
        for i in range(rlen):
            if len(arr[i]) < maxLen:
                arr[i] = arr[i] + [0] * (maxLen - len(arr[i]))
        clen = maxLen

#c 연산
    else:
        maxLen = -1
        appendList = deque([])
        for i in range(clen):
            checkList = []
            col = list(zip(*arr))[i]
            for j in range(rlen):
                num = col[j]
                if num > 0:
                    if [num, col.count(num)] not in checkList:
                        checkList.append([num, col.count(num)])
            checkList.sort(key=lambda x: (x[1], x[0]))
            col = sum(checkList, [])
            maxLen = max(maxLen, len(col))

            #for j in range(len(col))
            appendList.append(col)

        # maxLen과 같게 행 추가
        if rlen < maxLen:
           arr = arr + [[0] * clen for _ in range(maxLen - rlen)]

        idx = 0
        for i in range(len(appendList)):
            col = appendList[i]

            #0으로 채우기
            #if len(col) < maxLen:
                #col = col + [0] * (maxLen - len(col))
            for j in range(len(col)):
                arr[j][i] = col[j]

    # 0으로 채우기
        for i in range(clen):
            if len(appendList[i]) < maxLen:
                for j in range(len(appendList[i]), maxLen):
                    arr[j][i] = 0

        rlen = maxLen



