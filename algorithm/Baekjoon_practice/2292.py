#벌집 문제 
#수열 이용하는 문제

N = int(input())
first = 1
plus = 6
room = 1

if N == 1:
    print(1)

else:
    while True:
        first = first + plus
        room+= 1
        if N <= first:
            print(room)
            break
        plus += 6

# 1, 7, 19, 37 ... 차수가 진행될 때마다 +6씩 늘어나는 수열이다. 
# 입력 숫자가 1일 경우 방 1개를 지난다(시작을 포함하므로). 
# 1보다 크고 7보다 작거나 같을 경우 방 2개를 지난다. 
# 7보다 크고 13보다 작거나 같은 경우 방 3개를 지난다.