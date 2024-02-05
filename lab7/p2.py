toppings = {"Peperoni": 2, "Sausage": 2, "Onions": 1, "Peeper": 1.2, "Anchovies": 3}
name = input("Enter your name: ")
current_price = 15
for topping in toppings:
    confirmation = input(
        f"Do you want {topping} on your pizza? (y/anything other than y) "
    ) == "y" or (topping == "Anchovies" and name == "Darth")
    if confirmation:
        current_price += toppings[topping]
print(f"Total cost for {name} is ${current_price:.2f}")
