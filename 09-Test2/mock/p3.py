def f(array2D):
    for row in range(len(array2D)):
        row_sum = 0
        col_sum = 0
        for column in range(len(array2D)):
            row_sum += array2D[row][column]
            col_sum += array2D[column][row]
        if row_sum != col_sum:
            return False
    return True

if __name__=="__main__":
    print(f([[3,7,2],[4,2,5],[5,2,1]]))
    print(f([[3,7,2],[4,2,5],[9,2,1]]))