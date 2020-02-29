### 큐?   
목록 한쪽 끝에서만 자료를 넣고 다른 한쪽 끝에서만 자료를 빼낼 수 있는 자료구조이다. (First-In, First-Out)   
데이터가 입력한 순서대로 처리되어야할 경우에 사용합니다.   
큐에 새로운 데이터가 들어오면 큐 끝에 데이터가 추가되며 enqueue, 삭제될땐 첫번째 위치의 데이터가 삭제된다 dequeue. 

### 큐 구현
리스트로 구현하는 것은 가능하나 효율적이지는 않다. 왜냐면 리스트의 맨 처음 원소를 빼거나 더하는 것은 다른 원소들을 한칸씩 이동시켜야 되기 때문에 느리다. 따라서 양끝에서 더하거나 빼는 것이 빠르도록 설계된 collections.deque를 사용하거나 파이썬에서 제공하는 큐 모델을 이용해 구현하는 것이 효율적이다. 

+ collections.deque   
deque 는 double-ended queue의 줄인말로, 양 방향에서 데이터를 처리할 수 있는 자료구조이다. 처리속도가 O(1)로 매우 빠르다. 

```python
from collections import deque

dq = deque([])

dq.append(1)
dq.append(2)
dq.append(3)
dq.append(4)
print(dq) #deque([1,2,3,4])

print(dq.popleft()) #1
print(dq.popleft()) #2
```

+ module   
```python
import queue

q = queue.Queue()

q.put(1)
q.put(2)
q.put(3)
q.put(4)

print(q.get()) #1
print(q.get()) #2 

from collections import deque

class Queue(deque):
    def enqueue(self, x):
        super().append(x)
    def dequeue(self):
        super().popleft()
    def display(self):
        for node in self.__iter__():
            print(node)
```

