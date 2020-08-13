file = '../text_files/psych.txt'
with open(file)as f:
    try:
        contents = f.read()
    except FileNotFoundError:
        print(f"sorry the file {file} doesn't exist")
    else:
        words = contents.split()
        number_of_words = len(words)
        print(f"the file{file} has about {number_of_words} words")
