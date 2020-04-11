sosu = [0 for i in range(10001)]
sosu[1] = 1
for i in range(2, 98):
    for j in range(i * 2, 10001, i):
        sosu[j] = 1
m = int(input())
n = int(input())
sum = 0
min = 0
for i in range(n, m - 1, -1):
    if sosu[i] == 0:
        sum += i
        min = i
if sum == 0:
    print(-1)
else:
    print(sum, min, sep='\n')

# 출처: https://pacific-ocean.tistory.com/128?category=810810