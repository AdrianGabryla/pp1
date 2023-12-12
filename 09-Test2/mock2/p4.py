def f(arr):
    counter = 0
    for i in range(len(arr)):
        if arr[i] not in arr[:i] and arr[i] not in arr[i+1:]:
            counter += 1
    return counter

if __name__=="__main__":
    print(f([11,22,33,11]))
    print(f([11,22,11,11,22,35,27,11,22,14]))