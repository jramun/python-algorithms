from collections import deque

queue = deque()
queue.append('1')
queue.append('2')
queue.append('3')
print('Queue before pop  ', queue)
queue.popleft()
print('Queue after pop  ', queue)

stack = []
stack.append('1')
stack.append('2')
stack.append('3')
print('Stack before pop  ', stack)
stack.pop()
print('Stack after pop  ', stack)
