def Binarysearch(t,n,start,end):
    midpoint=(start+end)//2
    if t[midpoint]==n:
        return midpoint
    elif t[midpoint]>n:
        return Binarysearch(t,n,start,midpoint-1)
    elif t[midpoint]<n:
        return Binarysearch(t,n,midpoint+1,end)

def Binarysearchnum(t,n):
    return Binarysearch(t,n,0,len(t)-1)

print(Binarysearchnum([1,4,7,8,23,46,67,99,145],99))
