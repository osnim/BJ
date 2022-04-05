import sys
from collections import deque
from itertools import combinations

queue = deque()
queue.append([2, 3])
print(queue)
queue.append((1, 3))
queue.append((2, 3))
print(queue)
a = queue.popleft()
print(a)