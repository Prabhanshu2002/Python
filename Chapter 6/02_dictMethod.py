myDict = {
  "fast": "In a quick manner",
  "harry" : "A coder",
  'marks': [1,2,3,4,5],
  'anotherdict': {'Harry':'player'} #nested dictionary
}


# print(myDict.keys())     #print the keys of the dictionary
# print(myDict.items())     #print the keys of the dictionary
# print(myDict.values())   #print the (keys,values) for all contents of the dictionary
print(myDict)
updatedict = {
    'Rohit':'friend',
    'Rahul':'friend',
    'harry':'a dancer' #it will override value of same key name
}
myDict.update(updatedict)   #update the dictionary by adding key value pairs from updateDict
print(myDict)  

#Difference between .get and [] syntax in dictionary
print(myDict.get("harry"))     #return none if harry key is not found in the dictionary
print(myDict["harry"])         #throw an error if harry key is not found in the dictionary
