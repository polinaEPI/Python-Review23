def create_youtube_video(title,description):
	youtube_video={"title":title,"description":description,"likes":0,"dislikes":0,"comments":{}}
	return youtube_video

def like(youtube_video):
	if "likes" in youtube_video:
		 youtube_video["likes"]+=1
	return youtube_video

def dislike(youtube_video):
	if "dislikes" in youtube_video:
		 youtube_video["dislikes"]+=1
	return youtube_video 

def add_comment(youtube_video,username,comment_text):
	youtube_video["comments"][username]=comment_text
	return youtube_video

myVideo=create_youtube_video("my video", "so cool!")
myVideo=dislike(myVideo)
myVideo=add_comment(myVideo,"poli","hiiiiiiiiiiii")
for i in range(495):
	myVideo=like(myVideo)

print(myVideo)
