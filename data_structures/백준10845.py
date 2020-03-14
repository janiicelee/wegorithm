# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 여섯 가지이다.

# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

class Queue:
    def __init__(self):
        self.queue = []
 
    def push(self, num):
        self.queue.append(num)
 
    def pop(self):
        return self.queue.pop(0) if len(self.queue) != 0 else -1
 
    def size(self):
        return len(self.queue)
 
    def empty(self):
        return 1 if self.size() == 0 else 0
 
    def front(self):
        return self.queue[0] if self.size() != 0 else -1
 
    def back(self):
        return self.queue[-1] if self.size() != 0 else -1
 
import sys
num = int(sys.stdin.readline())
queue = Queue()
for _ in range(num):
    tokens = sys.stdin.readline().split()
 
    if tokens[0] == "push":
        queue.push(tokens[1])
    elif tokens[0] == "pop":
        print(queue.pop())
    elif tokens[0] == "size":
        print(queue.size())
    elif tokens[0] == "empty":
        print(queue.empty())
    elif tokens[0] == "front":
        print(queue.front())
    elif tokens[0] == "back":
        print(queue.back())
    else:
        print("it's not acceptable operator")