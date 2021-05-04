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
