def Merge_sort(n):
    return Merge_sort2(n,0,len(n)-1)

def Merge_sort2(n,first,last):
    if first<last:
        p=(first+last)//2
        Merge_sort2(n,first,p)
        Merge_sort2(n,p+1,last)
        return Merge(n,first, p+1,last)

def Merge(n,first,p,last):
    left=n[first:p]
    right=n[p:last]
    i=j=0
    for k in range(first,last+1):
        if left[i]<=right[j]:
            n[k]=left[i]
            i+=1
        else:
            n[k]=right[j]
            j+=1
    return n

print(Merge_sort([827,345,612,822,444,222,1,9]))
