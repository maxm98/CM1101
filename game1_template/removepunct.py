string = input("enter a string: ")

def removepunct(text):
    for i in text:
        if i.isalpha() == False:
            newstring = text.replace(i,"")
    print (newstring)
    return newstring

removepunct(string)
