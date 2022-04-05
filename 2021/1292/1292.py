import sys
A, B = map(int, sys.stdin.readline().split()) #공백을 기준으로 처음과 끝 입력 받기
arr = [] #1,2,2,3,3,3,4,4,4,4, .... 인 리스트를 만들어준다.

for i in range(1, 1001):
    for j in range(i):
        arr.append(i)
#print(arr)
sum = 0
for i in range(A-1, B): # A번째 숫자는 A-1번째 인덱스
    sum += arr[i]

print(sum)
