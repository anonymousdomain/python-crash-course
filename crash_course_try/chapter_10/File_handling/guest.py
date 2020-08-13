propmpt = 'welcome to our guest house '
propmpt += 'please enter your name enter quite to exite \n'

file = '../text_files/guest.txt'
active = True
user_names = ""
users = []
while active:
    user_names = input(propmpt)
    if user_names == 'quite':
        active = False
    else:
        print(f"hello {user_names}")
        users.append(user_names)

users.sort()
for user in users:
    wr = open(file, 'a')
    wr.write(f"{user}\n")

print('excuted')
