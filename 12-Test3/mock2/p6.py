def f(mnumbers):
    import re
    counter = 0
    for i in mnumbers:
        if re.search("^[A-Da-d]|'+'|'-'|[1-7].+[A-Da-d]|[1-7]&", i):
            counter += 1
    return counter

if __name__=="__main__":
    print(f(["A15","-31","7abC","+D1","-gH"]))
    print(f(["A05","-3+1","7ab8C","+D1","-22k"]))