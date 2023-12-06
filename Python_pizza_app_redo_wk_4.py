
print("Hi Im  PizzaBot., what do you want?")
print("Ok  look here im gonna ask you some questions, you answer press enter got it!?  ")


userName = input(f"\nHWhat your name?")
if userName.lower() == "Gene Shaffer":
    print(f"\nOh My God!!!!  Its him!!      Its Really him!!    What a pleasure to finally meet you")
else:
    print(f"\nHello {userName} nice to meet you. ")
   
    

size = input("\nWhat size do you want?  Enter  small,   medium, or  large:  ")
while len(size) == 0:
    size = input("Wrong answer  Enter small, medium, or large:  ")
    
flavor = input("\nWhat flavor?:  ")
while len(flavor) == 0:
    flavor = input("\nYou got to have some flavor, Enter a flavor:  ")
    
crustType = input("\nWhat style crust?:  ")
while len(crustType) == 0:
    crustType = input("\nWhat kind of crust?:  ")
    
quantity = input("\nHow many you want?   Enter a number value:  ")
quantity = int(quantity)

method = input("\nFor carry out or delivery?:  ")
while method not in ["carry out", "delivery"]:
    method = input("Not a valid entry! Enter carry out or delivery:  ")
if method.lower() == "delivery":
    deliveryFee = 5
else:
    deliveryFee = 0
    






salesTax = 1.1

if size.lower() == "small":
    pizzaCost = 8.99 
elif size.lower() == "medium":
    pizzaCost = 14.99
elif size.lower() == "large":
    pizzaCost = 17.99
    
total = (pizzaCost * quantity) * salesTax + deliveryFee

print("_" * 50)


print(f"Thank you {userName}, for your order.  ")
print(f"Your {quantity} {size} {flavor} pizza(s) with {crustType} crust costs ${total:,.2f}.")
if total >= 50:
    print("\n Congratulations! youve been awarded a $10 coupon for your next order!")
else:
    print("\nOrders over $50 recieve a free $10 off coupon!")
    


print("_" * 50)














