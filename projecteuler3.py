def LargestPrime(n):
    maxprime=0
    simplegen= (i for i in range(n,0,-1))
    for i in simplegen:
        count=0
        simplegen2= (j for j in range(1,i+1))
        for j in simplegen2:
            if i%j==0:
                count+=1
            if count>2:
                break
        if count==2 and n%i==0:
            maxprime=i
            return maxprime

print(LargestPrime(600851475143))
