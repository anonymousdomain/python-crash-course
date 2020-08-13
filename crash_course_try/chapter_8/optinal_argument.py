def get_formatted_name(firstName,lastName,middleName=''):
    if middleName:
         fullName=f"{firstName}{middleName}{lastName}"
    else:
        fullName=f"{firstName} {lastName}"
    return fullName
musician=get_formatted_name('kalkidan','manaze')
print(f"the young musician '{musician}' welcom")

musician=get_formatted_name('devo','tiller','.')
print(musician)
