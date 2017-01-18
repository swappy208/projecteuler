
def trianglenum():
    num=1
    while (True):
        total=0
        for x in range(1,num+1):
            total+=x
        factors=0
        for x in range(1,total+1):
            if total%x==0:
                factors+=1
        if factors>500:
            return total
        num+=1
print(trianglenum())
