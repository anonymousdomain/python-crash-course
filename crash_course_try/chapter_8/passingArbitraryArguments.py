# *used to pass arbitrary arguments

def making_pizza(*toppings):
    print(toppings)

making_pizza('paproni')
making_pizza('extra chees','olive','quark')

####################################################################################
def pizaWithSize(size,*toppings):
    print(f"your {size} sized pizza is made from:\n")
    for topping in toppings:
        print(f"{topping}")

pizaWithSize('large','extra chees','paproni','oilve','')