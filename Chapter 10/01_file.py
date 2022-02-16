# A file is data stored in a storage device. 
# A python program can talk to the file by reading content from it and writing content to it.

# Types of file
# i)text file (.txt, .c etc)
# ii)binary file (.jpg, .dat etc)



# python has a lot of functions for reading,updating and deleting files.

# Opening a file
# Python has an open() function for opening files. it takes 2 parameters: filename and mode

# open("this.txt","r")   --> where "r" is mode of opening(read mode)
#          |
#         file name
# open() is a built-in function



#reading a file
#Pyton has a read() function for read any file


# f = open("sampleChapter_10.txt",'r')           #open a file
# data = f.read()                                #read its contents
# print(data)                                    #print its contents
# f.close()                                      #close the file

# we can also specify the number of characters in read() function : f.read(2)   #it will read first 2 characters

# other method to read the file
# we can also use f.readline() function to read on full line at a time.

f = open("sampleChapter_10.txt",'r')           #open a file
data = f.readline()                                #read its contents
print(data)                                    #print its contents
data = f.readline()                                #read its contents
print(data)             
f.close()                                      #close the file

