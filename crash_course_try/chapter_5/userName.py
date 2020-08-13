userNames = ['dawit', 'devo', 'devid', 'dev', 'davencho', 'admin']
for userName in userNames:
    if userName == 'admin':
        print(f"hello {userName} how are u")

    else:
        print(f"hello {userName} thnaks for logging again")
        newUsernames = ['davido', 'Dawit', 'dbaby', 'Dev']
for newUsername in newUsernames:
    if newUsername.lower() in userNames:
        faildUserName=newUsername
        #print(f"the username {newUsername} is already in use try other username")
    else:
        acceptedUserName=newUsername
       # print(f" your new user created as {newUsername}")

print(f"faild user name:{faildUserName}")
print(f"accepted user name:{acceptedUserName}")