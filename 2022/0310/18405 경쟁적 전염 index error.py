import sys
from collections import deque

def BFS(virus, virusPositions):
    for i in range(len(virusPositions[virus])):
        a, b = virusPositions[virus].pop(0)

        for j in range(4):
            nx = a + dx[j]
            ny = b + dy[j]

            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                if virusGraph[nx][ny] == 0:
                    virusGraph[nx][ny] = virus
                    virusPositions[virus].append([nx, ny])

virusGraph = []

N, K = map(int, sys.stdin.readline().split())
for i in range(N):
    virusGraph.append(list(map(int, sys.stdin.readline().split())))

virusPositions = [[] for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        if virusGraph[i][j] != 0:
            virusPositions[virusGraph[i][j]].append([i, j])

S, X, Y = map(int, sys.stdin.readline().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(S):
    for virusNum in range(1, K+1):
        if not virusPositions[virusNum]:
            continue
        BFS(virusNum, virusPositions)

print(virusGraph[X-1][Y-1])