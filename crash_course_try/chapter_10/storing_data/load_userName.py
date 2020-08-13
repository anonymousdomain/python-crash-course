import json
"""load the userName from the JSON file"""
file_name='userName.json'
with open(file_name)as f:
   username= json.load(f)
print(f"welcome back {username}")