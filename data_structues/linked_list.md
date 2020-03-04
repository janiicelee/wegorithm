## Linked list   
+ element간의 연결(link)을 이용하여 리스트 구현.
+ 연결이 무엇인가를 파악하는 것이 중요하다. 
+ 여기서 '연결된 엘리먼트'들은 node, 혹은 vertex라고 한다. 

## Dummy linked list
+ 실제 데이터를 가진 node가 아닌, 구현의 편의를 위해 앞에 두는 무의미한 노드
+ 노드를 단위로 한다. 노드가 다음 노드로 아무것도 가리키지 않으면 리스트의 끝이다.

## Node
+ 노드는 자료와 다음 노드를 가리키는 참조값으로 구성되어있다.   
```python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
```

##### 본 자료는 '초보몽키의 개발공부로그'를 참고했습니다.