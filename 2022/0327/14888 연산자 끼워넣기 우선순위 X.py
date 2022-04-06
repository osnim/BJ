import sys
import itertools
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
tempOp = list(map(int, sys.stdin.readline().split()))
opList = []
MIN = int(1e9)
MAX = int(-1e9)

k = -1
for i in tempOp:
    for j in range(i):
        opList.append(k)
    k -= 1

op = list(itertools.permutations(opList, len(opList)))
# - 있는 경우 -로 바꿔주기

for i in op:
    tmp = []
    tempNum = num[:]
    result = [0]
    for j in range(len(i)):
        # +연산
        if i[j] == -1:
            tmp.append('+')
            result[0] = tempNum[0] + tempNum[1]
            tempNum.pop(0)
            tempNum.pop(0)
            tempNum = result + tempNum
        elif i[j] == -2:
            tmp.append('-')
            result[0] = tempNum[0] - tempNum[1]
            tempNum.pop(0)
            tempNum.pop(0)
            tempNum = result + tempNum
        elif i[j] == -3:
            tmp.append('*')
            result[0] = tempNum[0] * tempNum[1]
            tempNum.pop(0)
            tempNum.pop(0)
            tempNum = result + tempNum
        elif i[j] == -4:
            tmp.append('/')
            if tempNum[0] < 0 :
                result[0] = -tempNum[0] // tempNum[1]
                result[0] = -result[0]
            elif tempNum[1] < 0:
                result[0] = tempNum[0] // -tempNum[1]
                result[0] = -result[0]
            else:
                result[0] = tempNum[0] // tempNum[1]
                result[0] = result[0]

            tempNum.pop(0)
            tempNum.pop(0)
            tempNum = result + tempNum
        else:
            print('Error')

    MIN = min(result[0], MIN)
    MAX = max(result[0], MAX)

print(MAX)
print(MIN)

