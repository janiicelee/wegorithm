#Generator Expression
#순회가능하고 일정 규칙 내의 숫자들을 반환하는 자료구조 사용
#합을 구하는 예시

def sum_generator(N):
    return sum(n for n in range(1, N+1))