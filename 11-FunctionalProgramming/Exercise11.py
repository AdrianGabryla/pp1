dis = 70
hour = 1
minu = 23
speed = lambda x,y,z: x/(y+z/60)
print(round(speed(dis,hour,minu), 2))