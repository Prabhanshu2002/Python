# # def my_function(fname, lname):
# #      print(fname + " " + lname)
# # my_function("Amit","Katoch")

# # def my_function(*kids):
# #       print("The youngest child is " + kids[1])
# # my_function("purva","sandesh","jiyansh") 

# # def my_function(**kid):
# #     print("Her last name is " + kid["lname"])
# # my_function(fname = "nitu", lname = "mini")
# # Abhishek Bhardwaj11:01 AM
# def subtract(x=0, y=0):
#     return x - y

# def multiply(x=0, y=0):
#     return x * y

# def divide(x=0, y=1):
#     return x / y

# def addition(x=0,y=0):
#     return x+y


# while True:
#     print("Select operation.")
#     print("1.Add")
#     print("2.Subtract")
#     print("3.Multiply")
#     print("4.Divide")
    
#     choice = input("Enter choice(1/2/3/4): ")


#     if choice in ('1', '2', '3', '4'):
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))





gvar="i'm global"
def var1():
    x = "i'm local "
    y = "i'm return"
    print(x)
    print(gvar)
    return y
# print(x) #Na
# 
# meError: name 'x' is not defined
print(gvar)
print(var1())
    