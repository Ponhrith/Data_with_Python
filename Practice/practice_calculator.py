apple_price = 2.5
banana_price = 3.5
strawberry_price = 4.5

while True:
    apple_amount = int(input("Enter the amount of apple you want: "))
    banana_amount = int(input("Enter the amount of banana you want: "))
    strawberry_amount = int(input("Enter the amount of strawberry you want: "))

    total_cost = (apple_amount * apple_price) + (banana_amount * banana_price) + (strawberry_amount * strawberry_price)

    if total_cost > 100:
        discount = total_cost * 0.2  
        total_cost -= discount
    elif total_cost > 50:
        discount = total_cost * 0.1  
        total_cost

    print(f"Your total is: ${total_cost:.2f}")

    choice = input("If you want to continue, press 'c'. To exit, press 'x': ").lower()
    if choice == 'x':
        print("You have exited the program.")
        break
