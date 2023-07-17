def create_youtube_video(title, description):
	new_video={"title":title, "description":description, "likes":0, "dislikes":0, "comments": {"username": ""},"hashtag":["","","","",""]}
	for i in range(5):
		new_video["hashtag"][i]=input("Add a hashtag: ")
	return new_video
def similarity_to_video(video1,video2):
	c=0
	for i in range(5):
		if video1["hashtag"][i] in video2["hashtag"]:
			c+=1
	return str((c/5)*100) + "%"
def like(new_video):
	if "likes" in new_video:
		new_video["likes"]+=1
	return new_video
def dislike(new_video):
	if "dislikes" in new_video:
		new_video["dislikes"]+=1
	return new_video
		
def add_comment(youtubevideo, username, comment_text):
	youtubevideo["comments"][username]= comment_text
	return youtubevideo 

example= create_youtube_video("cats","we love cats")
print(example)
like(example)
dislike(example) 
add_comment(example, "nour","wow")
print(example)
for i in range(495):
	like(example)
print(example)

example2= create_youtube_video("hi","wohooo")
print(similarity_to_video(example,example2))
