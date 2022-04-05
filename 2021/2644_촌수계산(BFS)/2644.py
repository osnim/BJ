import sys
from collections import deque

def BFS(begin, end):

    distance = 0  # start와의 거리
    deq = deque([[begin, distance]])

    #deq.append([begin, distance])
    visit = [False] * (N+1)

    while deq:
        deq_value = deq.popleft()
        distance = deq_value[1]

        if deq_value[0] == end:
            return deq_value[1]

        if visit[deq_value[0]] == False:
            visit[deq_value[0]] = True
            distance += 1

            #인접 노드 큐에 추가 -> 다음 방문 할 예정
            for i in graph[deq_value[0]]:
                #print("i = ",i,)
                if visit[i] == False:
                    deq.append([i, distance])
                    #print(deq)

    return -1

# 전체 사람 수
N = int(input())

#촌수를 계산해야 하는 서로 다른 두 사람의 번호
M, K = map(int, sys.stdin.readline().split())

# 부모 자식들 간 관계의 개수
R = int(input())

graph = [[] for _ in range(N+1)]

#관계 있는 숫자 모두 저장 (1번 이면 1번 리스트에 저장)
for _ in range(R):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)      #자식 저장
    graph[y].append(x)      #부모 저장

#print(graph)

print(BFS(M, K))


