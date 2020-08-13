file= '../text_files/programing.txt'
with open(file,'w') as file_object:
    file_object.write('i love to program\n')

with open(file,'a') as file_object:
    file_object.write('i also love finding meanings i large dataset')
    
