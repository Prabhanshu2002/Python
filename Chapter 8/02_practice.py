num1 = int(input("Enter Your Num1: "))
num2 = int(input("Enter Your Num2: "))
num3 = int(input("Enter Your Num3: "))
num4 = int(input("Enter Your Num4: "))

if(num1>num2)&(num1>num3)&(num1>num4):
    print("Num1 is Greater",num1)
elif(num1<num2)&(num2>num3)&(num2>num4):
    print("Num2 is Greater",num2)
elif(num3>num1)&(num3>num2)&(num3>num4):
    print("Num3 is Greater",num3)
else:
    print("Num4 is Greater",num4)

