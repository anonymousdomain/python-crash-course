#range function used to itrate numbers off by one
#examples range(1,5) will cause to itrate [1,2,3,4]
for n in range(1,5):
    print(n)

numbers=list(range(1,6))#store values in a list
print(numbers)

even_num=list(range(2,15,2))#start form 2 & the last parameter(2) cause to add(2) until it reachs the limt (15)
print(f"even:{even_num}")