foods = []
prices = []
total = 0

while True:
    food = input("Enter a food name(q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: ₹ "))
        quantity = int(input(f"Enter the quantity of a {food}: "))
        tot = price * quantity
        foods.append(food)
        prices.append(tot)

print("======= YOUR CART ======")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"Your total is: ₹{total}")