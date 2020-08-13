prompt="say somthing & i will repeat it back to u\n"
prompt+="enter quite to end the program\n"
active=True #flag
message=""
while message ==active:
    message=input(prompt)
    if message=='quite':
        active=False
    else:
       print(message)