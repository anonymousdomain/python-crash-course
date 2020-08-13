programming_languges={'dawit':'java',
                      'nahom':'c#',
                      'eliab':'python',
                      'samuel':'c++'}
#looping through all key value pair

for k,v in programming_languges.items():#items() method to pull out key value pair
    print(f"{k}'s favorite languges is {v}")
print()
#pull out only keys  >>>>keys()
print("key values")
for k in programming_languges.keys():
    print(f"{k}")
