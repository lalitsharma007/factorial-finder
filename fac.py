
def lalit(n):
    fac=1
    for i in range(n):
        fac=fac * (i+1)
    return  fac
number=int(input("enter your number:"))
print('Your Ans is', lalit(number))
