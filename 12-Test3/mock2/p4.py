def f(fnc,res):
    results = list(filter(fnc, res))
    return max(results)-min(results)

if __name__=="__main__":
    print(f(lambda x: x>50, [95,90,20,50,70]))
    print(f(lambda x: x>30 and x<90, [95,90,20,50,70]))