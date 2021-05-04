'''
# 상화좌우
n = int(input())
datas = input().split()
x, y = 1, 1

move = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for data in datas:
    for i in range(len(move)):
        if data == move[i]:
            nx = x+dx[i]
            ny = y+dy[i]
    if ny < 1 or nx < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
'''

'''
# 시간
n = int(input())
count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
'''

'''
# 왕실의 나이트
n = input()
row = int(n[1])
col = int(ord(n[0]))-int(ord('a'))+1

moves = [(1, 2), (-1, 2), (1, -2), (-1, -2),
         (2, 1), (-2, 1), (2, -1), (-2, -1)]
count = 0

for move in moves:
    next_row = row+move[0]
    next_col = col+move[1]
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        count += 1

print(count)
'''

'''
# 게임 개발
n,m=map(int, input().split())

d=[[0]*m for _ in range(n)]
x,y,direction=map(int, input().split())
d[x][y]=1

array=[]
for i in range(n):
  array.append(list(map(int,input().split())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def turn_left():
  global direction
  direction -=1
  if direction == -1 :
    direction=3

count=1
turn_time=0
while True:
  turn_left()
  nx=x+dx[direction]
  ny=y+dy[direction]
  if d[nx][ny]==0 and array[nx][ny]==0:
    d[nx][ny]=1
    x=nx
    y=ny
    count +=1
    turn_time=0
    continue
  else :
    turn_time+=1
  if turn_time==4:
    nx=x-dx[direction]
    ny=x-dy[direction]
    if array[nx][ny]==0:
      x=nx
      y=ny
    else:
      break
    turn_time=0

print(count)
'''
