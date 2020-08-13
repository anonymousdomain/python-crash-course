alien_0 = {'color': 'green', 'points': 10}
# accessing value in Dictionaries
print(f"u just earned {alien_0['points']} points")

# adding a new key value pair
alien_1 = {'name_of_aline': 'xcodek4', 'x coordinate': 0, 'y coordinate': 50}
print(alien_1)
# modifiyng value
alien_1['x coordinate'] = 50
print(alien_1)
# removing key value pair from dictinary
del alien_1['name_of_aline']
print(alien_1)
# giving a default value>>>using special method get()
name = alien_1.get('name_of_aline', 'the name was removed from the dictinary')
print()
print(name)
