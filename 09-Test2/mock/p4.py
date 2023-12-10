def f(subjects):
    largest_sub = ""
    largest_gra = 0
    for key, value in subjects.items():
        avg = 0
        for i in value:
            avg += i
        avg = avg/len(value)
        if avg > largest_gra:
            largest_gra = avg
            largest_sub = key
    return largest_sub

if __name__=="__main__":
    print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))