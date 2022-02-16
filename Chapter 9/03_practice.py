def maximum(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    
    else:
        if(num2>num3):
            return num2
        else:
            return num3
num1 = int(input("Enter Your Num1: "))
num2 = int(input("Enter Your Num2: "))
num3 = int(input("Enter Your Num3: "))
m = maximum(num1,num2,num3)
print("The value of the maximum is " + str(m)) 












