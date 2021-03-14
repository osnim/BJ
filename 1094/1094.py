import sys
X = int(sys.stdin.readline().rstrip())

stick = 64
count = 0  #막대기 개수
sum = 0    #붙인 막대기 길이

if X == stick:
    print(1)
    exit(0)

while(True):

    stick /= 2

    stick = int(stick)

    if stick < 1:
        break

    sum += stick   #일단 붙이기
    count += 1

    if sum == X:
        break

    if stick > X:
        sum -= stick  # 나눈 막대를 붙이지 않기, 실행 취소
        count -= 1
        continue #나눈 막대를 붙이지 않고 반으로 나누는 거 다시 실행

    elif stick < X:     #나눈 막대기가 X보단 작지만
        if sum > X:     #막대를 잘라서 붙였는데 X보다 큰 경우
            sum -= stick #나눈 막대를 붙이지 않기, 실행 취소
            count -=1

print(count)

