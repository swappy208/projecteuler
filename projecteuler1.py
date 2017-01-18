def Multi(n):
    s=0
    for number in range(0,n):
        if number%3==0 or number%5==0:
            s+=number
    return s

print(Multi(10))
