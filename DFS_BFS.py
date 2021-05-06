'''
# stack
stack=[]

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])
'''

'''
# queue
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)
'''

'''
# 재귀함수 무한
def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()


recursive_function()
'''

'''
# 재귀함수 종료
def recursive_function(i):
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀 함수를 종료합니다.')


recursive_function(1)
'''

'''
# 반복 구현
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


print(factorial_iterative(5))

# 재귀 구현
def factorial_iterative(n):
    if n <= 1:
        return 1
    return n * factorial_iterative(n-1)


print(factorial_iterative(5))
'''

'''
# 인접 행렬
INF = 999999999

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)

# 인접 리스트
graph = [[] for _ in range(3)]

graph[0].append((1, 7))
graph[0].append((2, 5))
graph[1].append((0, 7))
graph[2].append((0, 5))

print(graph)
'''
