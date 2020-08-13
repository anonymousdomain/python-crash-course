def greates_album_of_all_the_time(albumTitle,artistName):
    fullInfo={'album':albumTitle,'artist':artistName}

    return fullInfo
Active=True#flag
while Active:
    albumN=input("tell us ur favorite albums you never forget\n")
    artistN=input("tell us name of the artist\n")

    repeat=input("do you wanna repeat?(yes/no)\n")

    gr=greates_album_of_all_the_time(albumN,artistN)
    if repeat=='no':
        Active=False
for k,v in gr.items():
    print(f"name of album:{k} & name of artist is:{v}")
