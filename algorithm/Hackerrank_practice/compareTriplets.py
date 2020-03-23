def compareTriplets(a, b):
    a_point = 0
    b_point = 0

    for i in range(len(a)):
        if a[i] < b[i]:
            b_point += 1
        elif a[i] > b[i]:
            a_point += 1
    return (a_point, b_point)
            