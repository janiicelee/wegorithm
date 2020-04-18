#피타고라스 문제
#주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

import sys

for line in sys.stdin:
    a, b, c = map(int, line.split())

    if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == b**2 + a**2:
        if a==b==c==0:
            break
        else:
            print("right")
            pass
    else:
        print("wrong")