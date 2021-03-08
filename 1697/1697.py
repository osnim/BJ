import sys
from collections import deque

MAX = 100001

N, K = map(int, sys.stdin.readline().split())

visit = [0] * 100001 #방문한 곳인지 체크 이자 경과 시간 측정

deq = deque() #deque 는 양쪽에서 입출력 가능
deq.append(N) #처음 시작점 : N

#BFS
while deq:
    x = deq.popleft()

    if x == K : #동생의 위치
        print(visit[x])
        break
    for i in (x+1, x-1, 2*x): # 범위 i+1, i-1, 2*i를 탐색
        if 0 <= i < MAX and not visit[i]:
            visit[i] = visit[x] +1
            deq.append(i)





