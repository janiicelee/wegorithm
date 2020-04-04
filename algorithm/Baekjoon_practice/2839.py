#설탕배달 문제
#N=a*5 + b*3이 되도록 하는 a+b의 최솟값을 구하라. 

n = int(input())
F = n//5
n%=5
T = 0
while F>=0:
    if n%3 == 0:
        T = n//3
        n = n%3
        break
    F-=1
    n+=5
print((n==0) and (F+T) or -1)

# n = a*5 + k
# k = b*3 = i
# 계속 나머지가 생기면 어쩔 수 없이 a를 줄여 k를 5만큼 증가해야한다. 
# i가 가질 수 있는 값은 3으로 나눈 나머지이므로 0, 1, 2 뿐.
# i가 1일땐 k값에 5를 추가하면 되고 i가 2일땐 k값에 10을 추가해야 나머지가 발생하지 않는다.
# k + 5 = b*3 +1 +5


#출처: https://doorbw.tistory.com/60 [Tigercow.Door]