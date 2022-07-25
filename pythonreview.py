def create_youtube_video():
	title = input("Write your title")
	description = input ("description")
	newvideo = {"title": title, "description": description, "likes": 0, "dislikes": 0, "comments":{}}
	return newvideo

def comments(newvideo): 
	username = input ("user name")
	text = input ("text")
	newvideo["comments"][username]= text 
	return newvideo

def likes(newvideo): 
	if "likes" in newvideo:
		newvideo["likes"]+=1
	return newvideo

def dislikes(newvideo): 
	if "dislikes" in newvideo:
		newvideo["dislikes"]+=1
	return newvideo

video = create_youtube_video()
comments(video)
likes(video)
dislikes(video) 
print (video)

def likes(newvideo): 
	if "likes" in newvideo:
		newvideo["likes"]+=495
	return newvideo

