def Countnum(t,a,count):
    if a in t:
        c=t.pop(t.index(a))
        count+=1
    else:
        return count
    return Countnum(t,a,count)

def Countnumbers(t,a):
    return Countnum(t,a,0)

print(Countnumbers([4,56,11,33,88,99,2,3,3,11,33], 1))

def Countn(t,a):
    count=0
    t=sorted(t)
    if a in t:
        indexvalue=t.index(a)
    else:
        return 0
    while t[indexvalue]==a:
        count+=1
        indexvalue+=1
    return count

print(Countn([4,56,11,33,88,99,2,3,3,11,33], 11))
