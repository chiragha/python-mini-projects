menu = {"pizza": 130.00,
               "roll": 40.50,
               "popcorn": 60.00,
               "chai": 10.50,
               "chips": 10.00,
               "coffee": 30.50,
               "water": 30.00,
               "lemon juice": 40.25
}
cart = []
total = 0

print("--------- MENU ---------")
for key, value in menu.items():
    print(f"{key:10}: Rs {value:.2f}")
print("------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------ YOUR ORDER ------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: Rs {total:.2f}")