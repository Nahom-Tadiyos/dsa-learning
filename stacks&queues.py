#Stacks

stk = []
print(stk)

#append to top of stack - O(1)
stk.append(4)
stk.append(3)

print(stk)

#Pop from stack - O(1)
x = stk.pop

print(x)
print(stk)

#ask what is on the top of stack - O(1)
print(stk[-1])

#ask if something is int the stack - O(1)
if stk:
    print(True)

#Queues - First in First out

from collections import deque
q = deque()

print(q)

#Enqueue - ddd element to the right - O(1)
q.append(5)
q.append(6)
print(q)

#Dequeue - remove object from left - O(1)
q.popleft()
print(1)

#Peek from the left side - O(1)
q[0]

#Peek from the right side - O(1)
q[-1]

