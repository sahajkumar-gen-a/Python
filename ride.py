#Write a program to select a ride according to your preference. The ride is divided into two major categories: 1. Bike 2. Car And further, bikes and cars are divided into 2 subcategories. To give the user better selection options.
ride=input("enter your preference 1. Bike 2. Car=")
if ride=="1":
    b=input ("what you want 1=scooty 2=sport bike")
    if b=="1":
        print("you have selected scooty")
    elif b=="2":
        print("you have selected sport bike")
    else:
        print("you have selected wrong choice")
elif ride=="2":
    c=input ("what you want 1=tms 2=kavasaki ninja")
    if c=="1":
        print("you have selected tms")
    elif c=="2":
        print("you have selected kavasaki ninja")
    else:
        print("you have selected wrong choice")
else:
        print("you have selected wrong choice")