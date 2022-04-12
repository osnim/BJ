import sys
def check_route(N, L, route):
    ramp = [0] * N  # 경사로를 세웠는지 확인하기 위한 리스트
    for i in range(N - 1):
        if route[i] != route[i + 1]:  # 높이 차이가 있는 경우
            if abs(route[i] - route[i + 1]) > 1:  # 높이 차이가 1이 아닌 경우
                return False
            else:  # 높이 차이가 1인 경우
                if route[i] - route[i + 1] == 1:  # 높은 칸에서 낮은 칸
                    if i + 1 + L > N: return False
                    check = route[i + 1]  # 경사로를 세울 수 있는 높이인지 확인용
                    for j in range(i + 1, i + 1 + L):
                        if ramp[j] or route[j] != check: return False
                        ramp[j] = 1
                elif route[i] - route[i + 1] == -1:  # 낮은 칸에서 높은 칸
                    if i - L < -1: return False
                    check = route[i]
                    for j in range(i, i - L, -1):
                        if ramp[j] or route[j] != check: return False
                        ramp[j] = 1
    return True

input = sys.stdin.readline
N, L = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

cnt = 0  # 지나갈 수 있는 길의 수 기록

for r in MAP:  # 행 확인
    if check_route(N, L, r): cnt += 1

for c in range(N):  # 열 확인
    if check_route(N, L, [MAP[r][c] for r in range(N)]): cnt += 1

print(cnt)
