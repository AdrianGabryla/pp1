import random
def rand_elem(array):
    length = len(array)
    num = random.randint(0,length-1)
    return array[num]
tab = [1,2,3,4,5,6,7,8,9]
print(rand_elem(tab))