def plusMinus(arr):
    positive_num = 0
    negative_num = 0
    zero = 0

    for i in range(len(arr)):
        if arr[i] > 0:
            positive_num += 1
        elif arr[i] < 0:
            negative_num += 1
        elif arr[i] == 0:
            zero += 1
        
    p_pro = positive_num / len(arr)
    n_pro = negative_num / len(arr)
    z_pro = zero / len(arr)

    return print('%0.6f' %p_pro), print('%0.6f' %n_pro), print('%0.6f'%z_pro)