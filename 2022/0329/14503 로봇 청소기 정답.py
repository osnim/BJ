from _collections import deque

n,m=map(int,input().split())
vis=[[0]*m for _ in range(n)]
r,c,d=map(int,input().split())

a=[list(map(int,input().split())) for _ in range(n)]

dx,dy=[0,1,0,-1],[-1,0,1,0] #  북동남서


q=deque()
q.append((r,c,d))

res=1
while q:
    y,x,cur=q.popleft()
    a[y][x] = res
    temp=cur
    for i in range(4):
        # 북동남서 0 1 2 3 -> 후진: 2 3 0 1
        # 북동남서 0 1 2 3 -> 회전: 3 0 1 2
        temp-=1
        if temp==-1: temp=3
        yy, xx = y + dy[temp], x + dx[temp]
        if 0<=yy<n and 0<=xx<m and a[yy][xx]==0:
            res+=1
            a[yy][xx]=2
            q.append((yy,xx,temp))
            break
        elif i==3:
            temp=(cur+2)%4
            yy, xx = y + dy[temp], x + dx[temp]
            if a[yy][xx]==1: print(res)
            else: q.append((yy, xx, cur))  # 방향은 그대로