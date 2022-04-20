introString=input("Enter your introduction")
print(introString)
wordCount=1
characterCount=0
for i in introString:
    characterCount=characterCount+1
    if(i==' '):
        wordCount=wordCount+1
print('Number of words',wordCount)
print('Number of characters',characterCount)
