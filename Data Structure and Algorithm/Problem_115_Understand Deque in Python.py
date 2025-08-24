"""Design a Double-Ended Queue

Implement a class MyDeque using collections.deque that supports the following operations:

pushRight(x) → Insert integer x at the right end of the deque.

pushLeft(x) → Insert integer x at the left end of the deque.

popRight() → Removes and returns the element from the right end of the deque. If the deque is empty, return -1.

popLeft() → Removes and returns the element from the left end of the deque. If the deque is empty, return -1."""
from collections import deque

mydeque = deque([])

mydeque.append(100)
mydeque.append(200)
mydeque.append(300)
mydeque.append(400)

print(mydeque)

mydeque.appendleft(70)
mydeque.appendleft(50)
mydeque.appendleft(30)
print(mydeque)

mydeque.pop()
mydeque.pop()
print(mydeque)


mydeque.popleft()
mydeque.popleft()
print(mydeque)

# Output:
# deque([100, 200, 300, 400])
# deque([30, 50, 70, 100, 200, 300, 400])
# deque([30, 50, 70, 100, 200])
# deque([70, 100, 200])