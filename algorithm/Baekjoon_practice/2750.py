arr_size = int(input())
arr = list()

for i in range(arr_size):
    arr.append(int(input()))

arr.sort()

for i in arr:
    print(i)