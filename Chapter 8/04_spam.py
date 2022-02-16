text = input("Please write your text:\n")
spam = False
if("makes a lot of money" in text):
    print("Hlw",text)
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True


if(spam):
    print("This text is Spam")
else:
    print("This text is not spam",text)