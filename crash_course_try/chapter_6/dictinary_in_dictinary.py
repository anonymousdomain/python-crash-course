users={'dawit':{'first_name':'dawit','last_name':'mekonnen','location':'addis abeba'},
       'nahom':{'first_name':'nahom','last_name':'dejene','location':'addis abeba'},
       'eyuel':{'first_name':'eyuel','last_name':'sahlu','location':'addis abeba'},
       'mitu':{'first_name':'frehiwet','last_name':'abebaw','location':'bahirdar'}
       }

for username,userInfo in users.items():
    print(f"\nusername:{username}")
    fullName=f"{userInfo['first_name']} {userInfo['last_name']}"
    location=f"{userInfo['location']}"
    #pull out the value
    print(f"fullName:{fullName}\n location:{location}")