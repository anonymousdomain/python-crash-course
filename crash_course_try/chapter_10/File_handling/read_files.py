path = 'C:/Users/LENOVO/Desktop/vox1.txt'
with open(path) as hello_file:
    contents = hello_file.readlines()
str = ''
for line in contents:
    str += line.rstrip()
print(str)
print(len(str))
print()
""" python reads file as a string 
u need to convert to a numerical if u want  to works with value int() float()
example"""
with open('../text_files/hello.txt') as h:
    var = h.read()
# var must be converted to integer
x = int(var) + 4
print(x)

file=open('../text_files/dev.txt', 'a')
file.write('hello dawit')


file.read()