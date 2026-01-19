# Module 2 In-Class Activity Program 1
tank_size = float(input("How big is your car's gas tank: "))
current_tank = float(input("How many gallons are in your tank now: "))
price_gallon = float(input("What is the price of gas per gallon: "))
gas_needed = tank_size - current_tank
total_price = gas_needed * price_gallon

print(f"Your gas will cost ${total_price:.2f}")


