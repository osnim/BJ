def Spring_Summer(cnt):
    deadMemory = []
    for _ in range(cnt):
        age, x, y = trees.pop(0)
        #treeMap[x][y].pop(0)
        #만약 나이보다 양분이 많을 때
        if age <= ground[x][y]:
            ground[x][y] -= age
            trees.append([age + 1, x, y])
            if (age + 1) % 5 == 0:
                breeding.append([age+1, x, y]) # 겨울을 위해 미리 저장
        else: #만약 나이보다 양분이 적을 때 -> 사망 pop하기
            deadMemory.append([age, x, y])

    while deadMemory:
        age, x, y = deadMemory.pop()
        ground[x][y] += age // 2

def Summer(deadMemory):
    # 나무 사망, 양분으로
    while deadMemory:
        age, x, y = deadMemory.pop()
        #age, x, y = trees.pop(idx)
        ground[x][y] += age // 2

def Fall():
    while breeding:
        age, x, y = breeding.pop()
        for dx, dy in (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1):
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N:
                trees.insert(0, [1, ny, ny])
    return

def Winter():
    # 겨울
    for i in range(N):
        for j in range(N):
            ground[i][j] += Fertilizer[i][j]
    return

N, M, K = map(int, input().split())
ground = [[5]*N for i in range(N)]
trees = []
Fertilizer = []
breeding = []
treeMap = [[[] for _ in range(N)] for _ in range(N)]

# 겨울을 위해
for i in range(N):
    Fertilizer.append(list(map(int, input().split())))

for i in range(M):
    x, y, age = map(int, input().split())
    trees.append(list([age, x-1, y-1]))
    treeMap[x-1][y-1] = age

trees.sort()

for k in range(K):
    #trees.sort()
    Spring_Summer(len(trees))
    #Summer(deadMemory)
    if breeding:
        Fall()
    Winter()
    if not trees:
        break

print(len(trees))