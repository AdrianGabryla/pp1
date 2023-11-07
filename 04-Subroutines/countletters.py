def count_letters(string, x):
    a = 0
    for i in string:
        if i == x:
            a += 1
    return a
if __name__ == "__main__":
    print(count_letters("You never get a second chance to make a first impression", "e"))