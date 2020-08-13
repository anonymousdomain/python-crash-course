path='C:/Users/LENOVO/Desktop/pi.txt'
with open(path) as file:
    bir=file.read()

str=''
for line in bir:
    str+=line.strip()

birthdate=input("when is your birthdate?\n")

if birthdate in str:
    print('your birthday exist in pi')
else:
    print('your birthday doesnt exist')