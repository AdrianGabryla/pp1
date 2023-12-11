def f(arr):
    out = []
    num = [1,2,3,4,5,6,7,8,9,0]
    for i in arr:
        if len(i) >= 4 and len(i) <= 12 and i == i.lower() and "_" in i:
            for j in num:
                if str (j) in i:
                    out.append(i)
    out = set(out)
    return len(out)

if __name__=="__main__":
    print(f(["uek","wa6ter8_7_x","anna.may","a_4b_c_d_e_f"]))
