armstrong_num=int (input("Enter 3 digit number "))
num=armstrong_num
sum=0
while num>0:
    d=num%10
    sum=sum+d**3
    num=num//10
if sum==armstrong_num:
    print("it is an armstrong_num")
else:
    print("it is not an armstrong_num")