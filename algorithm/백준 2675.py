num = int(input())
result = str()

for i in range(num):
    num_r, test_str = input().split()
    num_r = int(num_r)
    for j in test_str:
        result = result + (j*num_r)
    print(result)
    result = str()