propmpt = 'welcome to the poll\n'
propmpt += 'please enter your name enter quite to exite \n'

active = True
responses = {}
while active:
    names = input(propmpt)
    response = input("why do you like programing languge?")
    responses[names] = response
    repeat = input("anyone wanna go? yes/no \n")
    if repeat == "no":
        active = False

for k,v in responses.items():
    file=open('../text_files/poll.txt', 'a')
    file.write(f"names:{k}\t\tresaons:{v} \n")

print("excuted")
