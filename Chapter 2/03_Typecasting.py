#Typecasting is a way to exchange one data types to another data types if Possible.
a ="3435" # Here a stores String Value.
print(type(a))
print(a + 5)
#It will give error bcz of 
#we try to add an integer to a string.

a = int(a)

print(type(a))
print(a)
