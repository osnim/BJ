import sys
num = int(sys.stdin.readline().rstrip())

for i in range(num):
    result = 0
    parenthesis = sys.stdin.readline().rstrip()

    if parenthesis[0] == ')':
        print('NO')
        continue

    for j in parenthesis:

        if j == '(':
            result += 1
            #continue

        elif j == ')':
            result -= 1
            #continue

        if result < 0 :
            break

    if result == 0:
        print('YES')

    else:
        print('NO')
