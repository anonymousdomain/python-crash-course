def get_formatted_name(first, last, middle=''):
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()


def accept_names():
    print("enter your full name enter q any time if you wanna quite\n")
    while True:
        first_name = input('enter your first name\n')
        if first_name == 'q':
            break
        last_name = input('enter your last name\n')
        if last_name == 'q':
            break
        formatted_name = get_formatted_name(first_name, last_name)
        print(formatted_name)


accept_names()
