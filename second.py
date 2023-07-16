def create_youtube_video(title, description):
	new_video={"title":title, "description":description, "likes":0, "dislikes":0, "comments": {"username": ""}}
	return new_video
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