#Write a program to check whether the student can take an exam or not. Students will be allowed only in two conditions: If they have a medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. If No, then check attendance If attendance is above 75, then allowed; otherwise, not allowed.
medecal_cause=input("medecal emergency:yes or no ")
print("medecal emergency")
if medecal_cause=="yes":
    print("Allloweḍ")
else:
    a=int (input("enter your attendence"))
    if a>=75:
        print("Allloweḍ")
    else:
        print("Not allloweḍ")