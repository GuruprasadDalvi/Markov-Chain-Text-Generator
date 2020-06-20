import random

def generateNextWord(currWord,tokens):
    chain=open("Chain.txt","r")
    chain=chain.read().split("\n")
    indexOfCurr=tokens.index(currWord)
    possiblities=chain[indexOfCurr].split(" ")
    if len(possiblities)>0:
        nextWord=possiblities[random.randint(0,len(possiblities)-1)]
        return nextWord
    else:
        return ""

def getDataFromYourSelf(Range):
    finalData=open("FilterdData.txt","a")
    for i in range(Range):
        currWord=beginWords[random.randint(0,len(beginWords)-1)]
        i=0
        while(currWord!=""):
            i=i+1
            #print(currWord,end=" ")
            currWord=generateNextWord(currWord,tokens)
            finalData.write(currWord+" ")
        #print('\n')
        print(str(j/100))


tokens=open("tokens.txt","r")
tokens=tokens.read().split("\n")
beginWords=open("Begin.txt","r")
beginWords=beginWords.read().split('\n')


for j in range(10):
    currWord=beginWords[random.randint(0,len(beginWords)-1)]
    i=0
    while(currWord!=""):
        i=i+1
        print(currWord,end=" ")
        currWord=generateNextWord(currWord,tokens)
    print('\n')
input("\n\n\nPress Any Key To Continue.....")