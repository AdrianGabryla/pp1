def f(arr):
    arr.sort()
    mid = arr[int(len(arr)/2)]
    first = arr[0]
    last = arr[-1]
    if first != mid:
        return first
    else:
        return last

if __name__=="__main__":
    print(f([7,7,7,7,7,5,7,7]))
    print(f([7,7,5]))
    print(f([7,7,7,7,7,5,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]))
    