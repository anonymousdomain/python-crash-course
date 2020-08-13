programing_languges={'dawit':['python','java','c++','css'],
                     'eliab':['python','ruby','javaScript'],
                     'kaleab':['java','c++','c#']}
for name,pr in programing_languges.items():
    print(f"favorite languges of {name}'s are:")
    for lan in pr:
        print(lan)
        if 'python'==lan:
            print(f"good choice {name}")
