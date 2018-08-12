import random

def roll():
    #Roll 2d6
    a = random.randint(1,6)
    b = random.randint(1,6)
    return [a,b]

i=0
while i<100000:
    r=roll()
    print r, sum(r)
    i+=1