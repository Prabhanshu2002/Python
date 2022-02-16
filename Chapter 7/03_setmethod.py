
b = set()

#To add element in set we use ".add" Method 
b.add(4)
b.add(3)
b.add(2)
b.add(4)    # adding value repeatedly does not change a set
# print(b)

#we can't add dict and list in set bcz list and dict can be change and tuple can be bcz tuple can't be change.
# b.add([])            #Try to add list in set
# b.add({6:5})         #TypeError: unhashable type: 'dict'
b.add((4,6,5,9,110))   #Addition of  tuple 
# print(b)

#Length of the set 
# print(len(b))   #return the length of a set

#removal of a element in set
# b.remove(3)     # it will remove 3 from the set if not available it will return error
# print(b)

#POP Method: it is used to remove an arbitrary elements from the set and return the element removed
# print(b.pop())
# print(b)
# print(b.pop())
# print(b)

