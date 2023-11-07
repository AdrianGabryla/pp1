def power(x, n):
    a = 1
    if n == 0:
        return a
    else:
        a = a * x
        n =- 1
        power(x, n)
if __name__ == "__main__":
    print(power(5, 3))