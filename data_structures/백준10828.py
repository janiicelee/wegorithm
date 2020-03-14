# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 다섯 가지이다.

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

class Stack():
    def __init__(self):
        self.list = []
        self.count = 0
    def push(self, value):
        self.list.append(value)
        self.count +=1
    def pop(self):
        if self.count == 0:
            return -1
        self.count -= 1
        return self.list.pop()
    def size(self):
        return self.count
    def empty(self):
        if self.count == 0:
            return 1
        else:
            return 0
    def top(self):
        if self.count == 0:
            return -1
        return self.list[-1]

import sys
stack = Stack()
N = int(sys.stdin.readline()) #시간초과 막기 위해
for i in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        stack.push(order[1])
    elif order[0] == 'pop':
        print(stack.pop())
    elif order[0] == 'size':
        print(stack.size())
    elif order[0] == 'empty':
        print(stack.empty())
    else:
        print(stack.top())