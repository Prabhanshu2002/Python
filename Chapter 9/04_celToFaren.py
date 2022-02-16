def fahren(cel):
    return (cel*(9/5)) + 32

celsius = int(input("Enter Temperature in Celsius: "))
print(f"Value of {celsius} Degree celsious in Fahrenheit is {fahren(celsius)}")