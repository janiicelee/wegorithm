#그룹단어가 아닌 것을 제외하는 방식
result = int(input())
for _ in range(result):
    word = input()
    for i in range(1, len(word)):
        if word.find(word[i-1]) > word.find(word[i]):
            result -= 1
            break
print(result)

#그룹단어인 것을 찾아가는 방식
result = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key = word.find)
        result += 1
print(result)