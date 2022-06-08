import random
def sorteia_dado():
    i=0
    x=0
    y=0
    z=0
    w=0
    f=0
    d=0
    while i <1000000:
        ale=(random.randint(1,6))
        i=i+1
        if ale == 1:
            x=x+1

        if ale == 2:
            y=y+1

        if ale == 3:
            z=z+1
        
        if ale == 4:
            w=w+1
        
        if ale == 5:
            f=f+1
        
        if ale == 6:
            d=d+1
        
    print("NÚMERO 1:",x)
    print("NÚMERO 2:",y)
    print("NÚMERO 3:",z)
    print("NÚMERO 4:",w)
    print("NÚMERO 5:",f)
    print("NÚMERO 6:",d)

sorteia_dado()