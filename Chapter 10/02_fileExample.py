

# f = open("sampleChapter_10.txt",'r')
# data = f.read()
# print(data)
# f.close()


# f = open("sampleChapter_10.txt",'w')
# data = f.write("Please write this to the file.")
# f.close()



f = open("sampleChapter_10.txt",'a')
data = f.write(" Please write this to the file(use with append). ")
f.close()