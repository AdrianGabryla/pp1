def second_largest_number(n):
    n.sort()
    return n[-2]
def difference(n1):
    n1.sort()
    return n1[-1]-n1[0]
def mediana(n2):
    n2.sort()
    if len(n2)%2==0:
        return (n2[len(n2)/2-1]+n2[len(n2)/2])/2
    else:
        return n2[int(len(n2)/2)]
def two_element(n3):
    n3.sort()
    return [n3[0],n3[-1]]
def minus_sign(n4):
    out = ""
    for i in n4:
        out = out + str(i) + '-'
    return out[:-1]