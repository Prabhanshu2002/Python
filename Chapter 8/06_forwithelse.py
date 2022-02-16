for num in range(1,10):
    print(num)
else: #Else will be executed after for loop naturally completed.
    print("Done")

for num in range(1,10):
    print(num)
    if num== 4:
        break
else:  #Here else will not execute bcz loop was not naturally completed its skiped. 
    print("Done")

#Error
# else:
    # print("Else after for loop will be valid not after any expression")