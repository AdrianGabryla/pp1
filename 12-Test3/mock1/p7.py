def f(arr2D):
    for row in range(0, len(arr2D)-1):
        for column in range(0, len(row)-1):
            #00+10+20==01+11+21/00+10==01+11==02+12
            sum1 += arr2D[column][row]
            sum2 += arr2D[column][row+1]