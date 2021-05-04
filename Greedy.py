'''
# 거스름돈
n = 1260
count = 0

coins = [500, 100, 50, 10]

for coin in coins:
    count += n // coin
    n %= coin

print(count)
'''

'''
# 큰 수의 법칙1
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]
result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)
'''

'''
# 큰 수의 법칙2
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]
result = 0

count = int(m/(k+1)) * k
count += m % (k+1)

result += first*count + second*(m-count)

print(result)
'''

'''
# 숫자카드 게임1
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_data = min(data)

result = max(result, min_data)
print(result)
'''

'''
# 1이 될때까지
n,m=map(int, input().split())
count=0

while n!=1:
  count+=1
  if n%m==0 : 
    n//=m
  else :
    n-=1

print(count)

'''
