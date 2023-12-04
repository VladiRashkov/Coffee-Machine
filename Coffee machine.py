
water = 300
milk = 200
coffee = 100
total_money = 0    
while True:
    # Espresso -> 50 ml Water // 18 g Coffee // 1.50 $
    def espresso(order, money):
        global water, coffee, total_money
        espresso_water = 50
        esspress_coffee = 18
        all_insterted_money = sum(money)

        if water >= espresso_water:
            water -= 50
        else:
            print("Sorry, there is not enough water. Money refunded.")
            return
        if coffee > esspress_coffee:
            coffee -= 18
        else:
            print("Sorry, there is not enough coffee. Money refunded.")
            return
        if all_insterted_money > 1.50:
            change = all_insterted_money-1.50
            total_money+=1.50
            print(f"Here is ${change:.2f} in change!")
            print("Here is your espresso. Enjoy!.")
        elif all_insterted_money==1.50:
            total_money+=1.50
            print("Here is your espresso. Enjoy!.")
        else:
            print("Sorry, that is not enough money. Money refunded.")

# Latte 100 ml Water // 24 g coffee // 150 ml Milk // 2.50 $
    def latte(order, money):
        global water, milk, coffee, total_money
        
        latte_water = 100
        latte_coffee = 24
        latte_milk = 150
        insterted_latte_coins = sum(money)
        
        if water >= latte_water:
            water-=latte_water
        else:
            print("Sorry, there is not enough water. Money refunded.")
            return
        if coffee>=latte_coffee:
            coffee-=latte_coffee
        else:
            print("Sorry, there is not enough coffee. Money refunded.")
            return
        if milk>=latte_milk:
            milk-=latte_milk
        else:
            print("Sorry, there is not enough milk. Money refunded.")
            return
       
        if insterted_latte_coins>=2.50:
            change_latte = insterted_latte_coins-2.50
            total_money+=2.50
            print(f"Here is ${change_latte:.2f} in change!")
            print("Here is your latte. Enjoy!.")
        elif insterted_latte_coins==2.50:
            total_money+=2.50
            print("Here is your latte. Enjoy!.")
        else:
            print("Sorry, that is not enough money. Money refunded.")

# Cappucciono 250 ml Water // 24 g Coffee // 100 ml Milk 3.00 $
    def cappuccino(order, money):
        global water, milk, coffee, total_money
        
        cappuccino_water = 250
        cappuccino_coffee = 24
        cappuccino_milk = 100
        insterted_cappuccino_coins = sum(money)
        
        if water >= cappuccino_water:
            water-=cappuccino_water
        else:
            print("Sorry, there is not enough water. Money refunded.")
            return
        if coffee>=cappuccino_coffee:
            coffee-=cappuccino_coffee
        else:
            print("Sorry, there is not enough coffee. Money refunded.")
            return
        if milk>=cappuccino_milk:
            milk-=cappuccino_milk
        else:
            print("Sorry, there is not enough milk. Money refunded.")
            return
       
        if insterted_cappuccino_coins>3.00:
            change_cappucciono = insterted_cappuccino_coins-3.00
            total_money+=3.00
            print(f"Here is ${change_cappucciono:.2f} in change!")
            print("Here is your cappuccino. Enjoy!.")
        elif insterted_cappuccino_coins==3.00:
            total_money+=3.00
            print("Here is your cappuccino. Enjoy!.")
        else:
            print("Sorry, that is not enough money. Money refunded.")

    order = input("What would you like? (espresso / latte / cappuccino): ")
    
    if order == "off":
        break
    if order == "report":
        print(f"Water: {water}ml" )
        print(f"Milk: {milk}ml" )
        print(f"Coffee: {coffee}g" )
        print(f"Money: ${total_money}" )
        continue
    
    quarters = float(input("how many quarters: "))*0.25
    dimes = float(input("how many dimes: "))*0.10
    nickles = float(input("how many nickels: "))*0.05
    pennies = float(input("how many pennies: "))*0.01
    money = [quarters, dimes, nickles, pennies]
    if order == 'espresso':
        espresso(order, money)
    elif order=='latte':
        latte(order, money)
    elif order=='cappuccino':
        cappuccino(order, money)
    else:
        print("No such drink! Please try again!")
        continue
    