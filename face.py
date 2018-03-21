def sendMail(msg,fdata):
    import fbchat
    try:
        client = fbchat.Client(fdata[0], fdata[1])

        friends = client.getUsers(fdata[2])  # return a list of names
        friend = friends[0]
        sent = client.send(friend.uid, msg)
    except:
        pass
    
