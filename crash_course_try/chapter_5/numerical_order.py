num = list(range(1, 15))
for numbers in num:
    if numbers==1:
        print(f"{numbers}st")
    elif numbers==2:
        print(f"{numbers}nd")
    elif numbers==3:
        print(f"{numbers}rd")
    elif numbers in range(4,15):
        print(f"{numbers}th")
