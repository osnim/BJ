num = int(input())    #수열 개수

stack = [] #파이썬에서 스택은 리스트
output = []
cnt = 1

check = True

for i in range(0, num):

    sequence = int(input())

    while cnt <= sequence:
        stack.append(cnt)
        cnt += 1
        output.append('+')

    if stack[-1] == sequence:
        stack.pop()
        output.append('-')

    else:
        check = False
        break
if check is True:
    for i in output:
        print(i)
else:
    print("NO")

# 처음에는 + - 를 바로 바로 출력하게 만들었는데
# 이렇게 하면 시간 초과가 뜬다.
# 그래서 한번에 출력하게 만들었다.

