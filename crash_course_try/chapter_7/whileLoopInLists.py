unconfirmedUsers=['caleb','wetifeta','abdukiar','gulumangecho']

confirmedUsers=[]

while unconfirmedUsers:
    currentUsers=unconfirmedUsers.pop()

    print(f"||verifying: {currentUsers}")
    confirmedUsers.append(currentUsers)
    
print("\n||this are verified users||")
for users in confirmedUsers:
    print(users)