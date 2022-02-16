
# def factorial(n):
#     product = 1
#     for i in range(n):
#         product = product * (i+1)
#     return product


n = int(input("Enter Any Number: "))

def factorial_recur(n):
    if n == 0 or n == 1 :
        return 1
    

    return n*(factorial_recur(n-1))

print(factorial_recur(n))