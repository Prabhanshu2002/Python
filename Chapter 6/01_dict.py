#Dictionary is a collection of key-value pair
# properties
#1. It is unodered
#2. it's value is mutable 
#3. it is indexed
#4. it can't contain duplicate keys


myDict = {
  "Fast": "In a quick manner",
  "Harry" : "A coder",
  'Marks': [1,2,3,4,5],
  'anotherdict': {'Harry':'player'} #nested dictionary
}

# print(myDict["Fast"])
# print(myDict["Harry"])
# print(myDict['anotherdict']['Harry'])
myDict['Marks'] = [224,252]
print(myDict['Marks'])