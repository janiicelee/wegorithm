#트리순회 문제
#dict사용하여 풀이
#https://daimhada.tistory.com/177 참조

import sys
input = sys.stdin.readline

#전위순회
def preorder(tree, root):
    stack = []
    stack.append(root)
    result = ''

    while 0 < len(stack):
        data = stack.pop()
        result += data

        if tree[data][1] != '.':
            stack.append(tree[data][1])

        if tree[data][0] != '.':
            stack.append(tree[data][0])
    
    print(result) #ABDCEFG

#중위 순회
def inorder(tree, root):
    stack = []
    result = ''
    data = root
    stack.append(root)

    while True:
        while tree[data][0] != '.':
            if data not in result:
                stack.append(tree[data][0])
                data = tree[data][0]
            else:
                break

        if 0 < len(stack):
            data = stack.pop()
            result += data

            if tree[data][1] != '.':
                stack.append(tree[data][1])
                data = tree[data][1]
        else:
            break

    print(result) #DBAECFG

#후위순회
def postorder(tree, root):
    stack = []
    result = ''
    stack.append(root)
    data = root

    while True:
        while tree[data][0] != '.':
            if tree[data][0] not in result:
                stack.append(tree[data][0])
                data = tree[data][0]

            else:
                break

        last_data = stack[-1]

        #오른쪽 자식이 존재하는지 먼저 확인
        if tree[last_data][1] == '.':
            result += stack.pop()

            if stack:
                data = stack[-1]
            else:
                break
        else: #오른쪽자식이 있으면 다음과 같이 해결
            if tree[data][1] not in result:
                stack.append(tree[data][1])
                data = tree[data][1]
            else:
                result += stack.pop()
                if 0 < len(stack):
                    data = stack[-1]
                else:
                    break
    print(result) #DBEGFCA

def solve(tree, root):
    preorder(tree, root)
    inorder(tree, root)
    postorder(tree, root)

if __name__ == "__main__":
    n = int(input().strip())
    tree = {}
    root = None
    for i in range(n):
        info = input().strip().split(' ')
        tree[info[0]] = [info[1], info[2]]

    solve(tree, 'A')
