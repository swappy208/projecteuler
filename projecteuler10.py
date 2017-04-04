import math
def summation(x):
    total=0
    for num in range(2,x+1):
        if prime(num):
            total+=num
    return total

def prime(x):
    for divisor in range(2,int(math.sqrt(x))+1):
        if x % divisor == 0 :
            return False
    return True

print(summation(2000000))
