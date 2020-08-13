import json

def get_stored_name():
    file_name = "userName.json"
    try:
        with open(file_name)as file:
            user_name = json.load(file)

    except FileNotFoundError:
        return None
    else:
        return user_name


def get_new_user():
    userName = input("what is your name?\n")
    file_name = "userName.json"
    with open(file_name, 'w')as f:
        json.dump(userName, f)
        return userName


def greet_user():
    userName = get_stored_name()
    if userName:
        print(f"welcome back {userName}")
    else:
        userName = get_new_user()
        print(f"we will remember when you comeback {userName}")


greet_user()
