import sys
from collections import deque

T = int(input()) #테스트 케이스 개수

def DFS(x):
    visit[x] = True
    a = permutation[x]

    #자기 자신
    if(a == x):
        return True

    if visit[a] == False:
        DFS(a)
        return True
    return False

for _ in range(T):
    cycle = 0
    N = int(input()) #순열 사이클의 개수
    visit = [False] * (N+1) #방문 했는지 확인 (DFS)

    # 공백을 기준으로 순열 입력 받기

    temp = [int(x) for x in input().split()]
    permutation = [0]
    permutation = permutation + temp #인덱스 1부터 세기 위해

    for i in range(1, N+1):
        if visit[i] == True:
            continue
        if DFS(i) == True:
            cycle += 1
    print(cycle)



