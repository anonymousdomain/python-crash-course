prompt="enter the city you want to visit"
prompt+="enter quite to end the program\n"

while True:
    message=input(prompt)
    if message=='quite':
        break
    else:
        print(f"i would love to visit {message.title()}")