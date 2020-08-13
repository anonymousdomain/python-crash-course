prompt = "enter two numbers two to calculate there addistion.\n"
print(prompt)
while True:
    try:
        f_num = int(input("enter the first number\n"))

        s_num = int(input("enter the second number\n"))

    except ValueError:
        print(f"invalid input string type can't  be calculated")
        break
    else:
        ans = f_num + s_num
    print(f"ans:{ans}")
