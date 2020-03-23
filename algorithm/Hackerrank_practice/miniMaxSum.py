def miniMaxSum(arr):
    new_arr = sorted(arr)
    minn = new_arr[:-1]
    maxx = new_arr[1:]
    print(sum(minn), sum(maxx))
    
