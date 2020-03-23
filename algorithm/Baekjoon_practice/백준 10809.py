str = input()
alist = [-1]*26

for i in range(len(str)):
    if alist[ord(str[i])-97] != -1:
        continue
    else:
        alist[ord(str[i])-97] = i
for i in range(26):
    print(alist[i], end = ' ')