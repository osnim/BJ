def compute():
    rlen = len(arr)
    clen = len(arr[0])
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
            # for j in range()
            # arr[i].append()
            arr[i] = arr[i] + [0] * (maxLen - len(arr[i]))
    return

r, c, k = map(int, input().split())
arr = []
r, c= r-1, c-1
ans = 0
for i in range(3):
    arr.append(list(map(int, input().split())))
while True:
    try:
        if arr[r][c] == k:
            print(ans)
            break
    except:pass
    if ans > 100:
        print(-1)
        break
    ans += 1

#R 연산
    if len(arr) >= len(arr[0]):
        compute()
    # c 연산
    else:
        arr = list(zip(*arr))
        compute()
        arr = list(zip(*arr))

