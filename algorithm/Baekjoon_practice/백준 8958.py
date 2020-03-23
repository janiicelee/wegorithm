n = int(input())
a = []
for i in range(n):
    O_score = 0
    X_score = 0
    total_score = 0
    a = input()
    for b in a:
        if b == 'O':
            O_score += 1
            total_score += O_score
        else:
            X_score = 0
            O_score = 0
    print(total_score)