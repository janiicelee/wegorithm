#람다 함수 사용하기 
#3,6,9만 string으로 표시하기
a = [x for x in range(1,10)]

print(a)

a = list(map(lambda x: str(x) if x%3==0 else x , a))
print(a)