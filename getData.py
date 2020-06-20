import json
import urllib.request
import emoji
import re

def filterOnlyLinks(comementList):
    #filters Links from Comment List
    filteredList=[]
    pat=re.compile(r'^https')
    for comment in comementList:
        if not pat.match(comment) and comment!='':
            filteredList.append(comment)
    return filteredList


def removeTimeStamp(commentList):
    #Removies Comments With Timestamp
    filteredList=[]
    pat=re.compile(r'\d[:.]\d')
    for comment in commentList:
        if not pat.search(comment):
            filteredList.append(comment)
    return filteredList

def removeNonEnglish(commentList):
    #removes Non English Commnents
    filterList=[]
    pat=re.compile(r'^[a-zA-Z0-9 &%,.]{3,}$')
    for comment in commentList:
        if pat.search(comment):
            filterList.append(comment)
    return filterList

def filterComments(comments):
    commentsFile=open("FilterdData.txt","a")
    comments=comments.split("\n")
    noEmoji=[]
    for comment in comments:
        noEmoji.append(removeEmoji(comment))
    comments=noEmoji
    comments=removeNonEnglish(comments)
    comments=removeTimeStamp(comments)
    comments=filterOnlyLinks(comments)
    for comment in comments:
        commentsFile.write(comment+"\n")




def removeEmoji(line):
    return emoji.get_emoji_regexp().sub(u'', line)

def getVideoIds():
    #returns All Video Ids From youtubeLinks.txt file
    links=open("youtubeLinks.txt","r")
    links=links.read().split("\n")
    listOfVideoIds=[]
    for link in links:
        if len(link)>10:
            listOfVideoIds.append(link.split('=')[1])
    return listOfVideoIds

def getCommentsFrom(VideoId):
    #store All Unfilterde Comments
    APIkey="AIzaSyAu-WXH7oDxw9x1rDS21BL2gNlWxEbvVdI"
    nextPageToken = ""
    url = f"https://www.googleapis.com/youtube/v3/commentThreads?key={APIkey}&textFormat=plainText&part=snippet&videoId={VideoId}&t&maxResults={100}&pageToken={nextPageToken}&start-index={0}"
    json_url = urllib.request.urlopen(url)
    data = json.loads(json_url.read())
    numberOfComments = len(data['items'])

    for i in range(numberOfComments):
        usernamesAndComments = f"{data['items'][i]['snippet']['topLevelComment']['snippet']['authorDisplayName']}\t{data['items'][i]['snippet']['topLevelComment']['snippet']['textDisplay']}".replace('\n'," ").replace('\r'," ")
        comments=usernamesAndComments.split("	")[1]
        filterComments(comments)


videoIds=getVideoIds()
for id in videoIds:
    getCommentsFrom(id)