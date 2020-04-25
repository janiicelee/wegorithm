## 팩토리얼 구하기
### 단순 반복문

```python
def factorial_for(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret
```

### 재귀함수
- 재귀함수는 함수 내에서 동명의 함수를 재호출하기 때문에, 함수를 무한히 호출해 스택오버플로우가 발생할 수 있어서 재귀의 탈출 조건(base case)를 정해줘야 한다. 
- 이 구현의 장점은 삼항 연산자(ternary operator)를 통해 1줄로 구현이 가능하다는 점인데 이때 조건이 ‘n > 1’이라는 것을 확인하면 된다. 팩토리얼은 0!과 1! 모두 1이다. 이 함수는 이 두 값 모두 1로 적절히 반환한다.

```python
def factorial_recursive(n):
    return n * factorial_recursive(n-1) if n > 1 else 1
```

### reduce 함수
- 함수형 프로그래밍에서, reduce는 fold라고 일컬어지는 함수 집합의 일원으로 재귀적인 자료구조를 분석하고 주어진 결합 동작을 사용해서 원 자료구조의 부분구조를 반복적으로 처리해 재결합해서 하나의 결과값으로 반환하는 고순위(higher-order) 함수이다.
- 파이썬의 리스트나 튜플 또는 range 처럼, 원소들을 하나씩 순회할 수 있는 자료구조를 뜻한다.
- 리스트 같은 자료구조는 원소의 개수가 임의적이다. 단 하나의 값이 아닌 상태다. reduce는 이런 자료구조에 결합동작(예를 들면, 합, 곱 등)을 사용해 원소들을 반복적으로 재결합해 하나의 값으로 반환한다.
- 예를 들어 [1, 2, 3, 4, 5]라는 리스트가 있을 때 모든 원소를 더한 ‘하나의 값’을 구하고 싶다면 ‘합(add)’라는 결합동작을 이용해 각 원소를 더해나가며 최종적인 값 15를 구할 수 있을 것이다. 이것이 reduce의 역할이다.
- 파이썬에서는 functools라는 내장 모듈에서 reduce라는 함수를 제공한다. 이 함수는 첫 번째 인자로 원하는 연산, 두 번째 인자로 재귀적인 자료구조를 받는다.

```python
from functools import reduce

def factorial_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n+1)
```

#### lambda x, y: x * y
- 첫 번째 인자로서 두 원소의 곱을 반환하는 익명 람다함수를 작성했다. 이 함수는 재귀적인 자료구조에서 (1, 2번째), (2, 3) 번째, (3, 4) 번째의 원소들을 차례로 곱해나가며 자료구조의 끝 원소까지 나아가 결국 단 하나의 곱값을 반환할 것이다.
#### range(1, n+1)
- 우리가 for 반복문에서 자주 사용하는 range 는 사실 재귀적인 자료구조다! 이는 파이썬의 중급 이상의 내용으로 이 포스트와 직접적인 관련이 없어 넘어간다.   
   
   

참고: https://shoark7.github.io/programming/algorithm/several-ways-to-solve-factorial-in-python



