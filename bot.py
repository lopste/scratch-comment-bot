import scratchconnect
import time

triggerBeep = "robot"

username = "username"
password = "password"
beepedComments = []
ecksdee = scratchconnect.ScratchConnect(username, password)
while True:
    time.sleep(1)
    currentComment = ecksdee.comments(1,1)[0]
    commentID = currentComment["CommentID"]
    if not commentID in beepedComments:
        beepedComments.append(commentID)
        if triggerBeep in currentComment["Content"]:
            ecksdee.connect_user(username).reply_comment("beep boop", commentID)
