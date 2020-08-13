import json
fileName='numbers.json'
numbers=[1,2,3,4,6,8,9]
with open(fileName,'w')as f:
    json.dump(numbers,f)

"""accept username & stor it to  JSON File"""

fileName='userName.json'
userName=input("what is your name?\n")
f=open(fileName,'w')
json.dump(userName,f)
print(f"we will remember you when you back {userName}")