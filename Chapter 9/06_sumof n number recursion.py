
def sum(num):
    if num == 0:
        return 0
    add = num + (sum(num-1))
    return add

num = int(input("Enter Last Number: "))

print(f"Sum of first {num} number is {sum(num)}")
