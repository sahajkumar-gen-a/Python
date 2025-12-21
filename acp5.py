r=0
n=int(input("enter any digit number this is nessesery "))
print("the number that you have entered is ",n)
while n>0:
    d=n%10
    r=r*10+d
    print("digit ",d)
    n=n//10
    print("number",n)
    print("result=",r)