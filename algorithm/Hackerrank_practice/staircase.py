def staircase(n): 
    for i in range(1, n+1): #1부터 n까지 범위설정 주의 
        stair = [] #한줄한줄 배열로 생각하기 

        for _ in range(n, i, -1):
            stair.append(" ")
        for _ in range(i):
            stair.append("#")
        print(''.join(stair))