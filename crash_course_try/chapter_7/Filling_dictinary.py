#empty dictinary
responses = {}
# use flag
active_polling = True

while active_polling:
    name = input("what is your name?\n")
    response = input("who is your favorite rapper")
    responses[name] = response
    repeat = input("\n would u like to another person respond? (yes/no)")

    if repeat.lower() == 'no':
        active_polling = False
#print the dictinary
print(responses)
