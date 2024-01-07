def f(fnc, prods):
    return ",".join(map(fnc, prods))

if __name__=="__main__":
    print(f(lambda x: "id:"+x[:2], ["water","cheese","tomato"]))
    print(f(lambda x: (x[0]+x[-1]).upper(), ["water","cheese","tomato"]))