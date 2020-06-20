
def makeTokens():
    data=open("FilterdData.txt","r")
    tonkens=open("tokens.txt","w")
    data=data.read().split('\n')#read data
    tokenList=[]
    for line in data:
        line=line.split(' ')
        for word in line:
            if word not in tokenList and word!=" ":
                tokenList.append(word)
                tonkens.write(word+'\n')
                print(word)
    #make tokens

def makeBeginWords():
    data=open("FilterdData.txt","r")
    begin=open("Begin.txt","w")
    data=data.read().split('\n')
    for line in data:
        line=line.split(" ")
        begin.write(line[0]+'\n')



def makeCahin():
    chainFile=open("Chain.txt","w")
    tokens=open("tokens.txt","r")
    data=open("FilterdData.txt","r")
    data=data.read().split("\n")
    tokens=tokens.read().split("\n")
    for token in tokens:
        possiblities=[]
        for line in data:
            line=line.split(" ")
            if (token in line) and(line.index(token)!=len(line)-1):
                if(line[line.index(token)+1]!=" "):
                    nextWord=line[line.index(token)+1]
                    possiblities.append(nextWord)
        for word in possiblities:
            chainFile.write(word+" ")
        chainFile.write("\n")

makeBeginWords()
makeTokens()
makeCahin()