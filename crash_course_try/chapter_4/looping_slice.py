names = ['dawit', 'nahom', 'eyuel', 'selam', 'mitu', 'tinu', 'birukty', 'ahmod']

for name in names[3:7]:
    print(f"kentuwa {name}")

# copy the list var[:]

my_list = ['java', 'python', 'css']
my_friends_list = my_list[:]


def dev():
    print(f"my list:")

    for my in my_list:
        print(my)


def friend():
    print("my friends list:")

    for friends in my_friends_list:
        print(friends)


dev()
friend()
my_list.append('java_script')
my_friends_list.append('ruby')
dev()
friend()
