from sys import stdin

line = list(stdin.readline().rstrip())
num = int(stdin.readline().rstrip())

temp_stack = []

for _ in range(num):
    input_cmd = stdin.readline()

    if input_cmd[0] == 'L' and line:   #커서 왼쪽으로 이동 = 임시 스택에 저장
        temp_stack.append(line.pop())

    elif input_cmd[0] == 'D' and temp_stack : # 커서 오른쪽으로 이동 = 임시스택에서 뺴기
        line.append(temp_stack.pop())

    elif input_cmd[0] == 'B' and line : # 커서 왼쪽 삭제
        line.pop()

    elif input_cmd[0] == 'P' :    #입력 = 스택에 추가
        line.append(input_cmd[2])


temp_stack.reverse()

line.extend(temp_stack)
print("".join(line)) # 리스트에서 문자열로 변환



