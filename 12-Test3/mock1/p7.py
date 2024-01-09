def f(arr2D):
    tab = []
    for column in range(0, len(arr2D[0])):
        sum1 = 0
        for row in range(0, len(arr2D)):
            sum1 += arr2D[row][column]
        tab.append(sum1)
    return len(tab)!=len(set(tab))

if __name__=="__main__":
    print(f([[3,4,2],[5,1,6]]))
    print(f([[3,4,2],[5,1,7]]))
    print(f([[3,4],[5,1],[4,7]]))
    print(f([[3,4],[5,9],[4,7]]))