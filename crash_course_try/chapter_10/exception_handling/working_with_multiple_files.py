def count_words(fileName):
    try:
        contents = open(fileName, encoding='utf-8')
        read_file = contents.readline()
    except FileNotFoundError:
        """ pass statment used to pass the error silently """
        # pass
        print(f"sorry the file {fileName} doesn't exist")
    else:
        words = read_file.split()
        couunt = len(words)

        print(f"the file {fileName} has about {couunt} words "
            ,f"& the word dawit exist {words.count('dawit')} times")


file_names = ['../text_files/guest.txt', '../text_files/hello.txt', '../text_files/psych.txt', '../text_files/poll.txt']
for fileName in file_names:
    count_words(fileName)
