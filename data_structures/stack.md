### 스택이란   
데이터의 삽입과 삭제가 저장소의 맨 윗부분에서만 일어나는 자료구조이다.   
스택은 데이터가 순서대로 저장되고 마지막에 넣은 요소가 제일 먼저 나가는 구조이다.(Last-In, First-Out)   
연속으로 저장된 데이터구조를 가지고 있고 맨 위 요소에 대한 포인터(주소값)를 갖는 Array나 linked list를 구현할 수 있다.   
스택 예시) 웹브라우저의 방문기록.

+ 장점: 참조 지역성(한번 참조된 곳은 다시 참조될 확률이 높다)을 활용할 수 있다.
+ 단점: 데이터를 탐색하기가 어렵다.

### 스택 ADT(Abstract Data Type)

+ push (-> None): 맨위에 값 추가.
+ pop (-> data): 가장 최근에 넣은 맨 위의 값을 제거.
+ peak (-> data or -1): 스택의 변형없이 맨 위의 값을 출력.
+ is_empty (-> boolean): 스택이 비어있는지 확인.

### 스택 구현 - list   
시간복잡도는 O(1) 이다.

```python
In [1]: def push(item):
   ...:     stack.append(item)
   ...: def pop():
   ...:     return stack.pop()
   ...: if __name__ == "__main__":
   ...:     stack = []
   ...:     push(1)
   ...:     push(2)
   ...:     push(3)
   ...:     print(stack)

[1, 2, 3]
```
### 스택 구현 - linked list   
연결리스트는 데이터를 노드 형태로 저장한 것을 말한다. 노드는 데이터와 다음 데이터 주소값을 가진다. 연결리스트의 헤드는 스택의 top을 가리킨다.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
        
    def push(self, data):
        new_mode = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def pop(self):
        if self.is_empty():
            return -1
        data = self.head.data
        self.head = self.head.next
        return data
    
    def is_empty(self):
        if self.head:
            return False
        return True
    
    def peek(self):
        if self.is_empty():
            return -1
        return self.head.data

```





