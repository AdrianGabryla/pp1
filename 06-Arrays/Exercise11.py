def month(n):
    month_name = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    return month_name[n-1]
if __name__=="__main__":
    print(month(1))
    print(month(9))
    print(month(12))