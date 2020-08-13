prompt="say somthing & i will repeat it back to u\n"

message=""
while message!='quite':
    message=input(prompt)
    if message!='quite':
       print(message)