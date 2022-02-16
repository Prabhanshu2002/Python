num = int(input("Enter the number: "))
prime = True
for i in range(2,num):
    if(num%i == 0):
        prime = False
        break

if prime:
    # print("This number",num,"is prime")
    print(f"{num} is prime number")
else:
    print("This number",num,"is not prime")