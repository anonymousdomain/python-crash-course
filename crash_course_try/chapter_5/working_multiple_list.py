available_toppings=['olives','mushrooms','green pappers','peppronies','peanaples','extrachees']
requasted_toppings=['mushrooms','olives','small papper']

for requasted_topping in requasted_toppings:
    if requasted_topping in available_toppings:
        print(f"adding {requasted_topping}")
    else:
        print(f"the requasted topping:{requasted_topping} are not available")