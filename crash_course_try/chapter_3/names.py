names = ['dawit', 'nahom', 'eyuel', 'selam', 'mitu', 'tinu', 'birukty', 'ahmod']

print(names[-1])

print(names[-3])

print(f"hey {names[-3]} how is your back haha")

# modifiying the list
names[5] = 'tina'
print(f"sorry i mean {names[-3]}")

vechil = ['motorcycle', 'bmw', 'lamborgini', 'jaguar', 'ferrari', 'ford']
# adding elements in a list
vechil.append('tesla car')
# append function add element at the last index

print(vechil)
#inserting element in to a list using insert function
#var.insert(postion,val)
vechil.insert(1,'toyota')
print(vechil)
#removing from a list using del
del vechil[1]
print(vechil)
#removing from a list using pop() remove from the last item
poped=names.pop()
print(f"removed item {poped}")
#removing from a list using pop() using postion
popV=names.pop(0)
print(popV)
#removing by value
names.remove('mitu')
print(f"i would like to own {vechil[-5]} one day")
