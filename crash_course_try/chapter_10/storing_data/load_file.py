import json

file_name='numbers.json'
with open(file_name) as file:
    numbers=json.load(file)
print(numbers)
