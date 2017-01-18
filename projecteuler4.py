def Palin():
    s=0
    m=0
    for a in range(999,0,-1):
        for b in range(999,0,-1):
            s=a*b
            num=str(s)
            if num==num[::-1] and s>m:
                m=s
    return m

print(Palin())
