#python interprate the input as string 
# so it needs to be casted to int

message=input("please enter your age :")
print(message)
#if message >=18:
   # print("u are old enough to vote")
    # this program will trough an error cuz it the input must be casted

if int(message) >=18:
    print("u are old enough to vote")
    


    #another way of casting x=int(input())