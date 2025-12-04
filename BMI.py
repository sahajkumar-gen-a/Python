W=int(input("Enter your weight "))
H=int(input("Enter your height "))
bmi=W/(H/100)**2
if bmi<18.5:
    print("underweight")
if bmi>18.5 and bmi<25.5:
    print("healthy")
else:
    print("Obese")