# * creates tuple for the remaining input 
def order_pizza(size, *toppings):
    if len(toppings) == 1:
        print(f"Ordered a {size} Pizza, with {toppings[0]}.")
    else:
        toppings_list = ", ".join(toppings[:-1])
        toppings_list += f" and {toppings[-1]}"
        print(f"Ordered a {size} Pizza, with {toppings_list}.")

# ** takes key value pair as argument
order_pizza("Small", "Capsicum", "Sweet corn", "Cheese")

def order_pizza_2(size, *toppings, **details):
    if len(toppings) == 1:
        print(f"Ordered a {size} Pizza, with {toppings[0]}.")
        for key, value in details.items():
            print(f"{key}: {value}")
    else:
        toppings_list = ", ".join(toppings[:-1])
        toppings_list += f" and {toppings[-1]}"
        print(f"Ordered a {size} Pizza, with {toppings_list}.")
        for key, value in details.items():
            print(f"{key}: {value}")

order_pizza_2("Large", "Capsicum", "Sweet corn", "Cheese", {Delivery:True}, {Tip:10})