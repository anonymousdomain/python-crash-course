print("enter two numbers & i will give you the division of two numbers")
print("enter q to end the program")

while True:
    first_number=int(input('enter the first number'))
    if first_number=='q':
        break
    second_numbers=int(input('enter the second number'))
    if second_numbers=='q':
        break
    try:
        ans = first_number / second_numbers
    except ZeroDivisionError:
        print("not divisble ba zero")


    print(f"ans:{ans}")