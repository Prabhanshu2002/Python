myDict = {
    'pankha':'fan',
    'dabba' : 'box'
}
print("Options are:",myDict.keys())
a = input("Enter the Hindi Word\n")
# print("The meanning of your word is:",myDict[a]) #this will throw an error if keys are not available
print("The meanning of your word is:",myDict.get(a)) # this will return none if keys are not available