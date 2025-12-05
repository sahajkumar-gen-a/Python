#Write a program to show students' grades by entering five subject marks and calculating average marks and grades. For example, if the average is between 91 to 100, A2 is between 81 to 90, and so on, do it till grade E2?
s1=100
s2=100
s3=99
s4=98
s5=100
total=s1+s2+s3+s4+s5
total_subjects=5
average=total/total_subjects
if average>90:
    print("A+")
elif average>81 and average<91:
    print("A")
elif average>70 and average<81:
    print("B+")
elif average>50 and average<71:
    print("B")
else:
    print("F")