
print("Hi Im  PizzaBot. How can I assist you today?")
print("Just going to ask a few questions, please press enter after your answer.  ")



userName = input(f"\nHEnter your name:  ")
while len(userName) == 0:
    userName = input("Name cannot be left blank!   Please enter your name:  ")
   
if userName.lower() == "Gene Shaffer":
    print(f"\nOh My God!!!!  Its him!!      Its Really him!!    What a pleasure to finally meet you!!  ")
else:
    print(f"\nHello {userName} nice to meet you. ")
   
    
size = input("\nWhat size do you want?  Enter  small,   medium, or  large:  ")
while size.lower() not in ["small" , "medium" , "large"]:
    size = input("Cannot be left blank!    Enter small, medium, or large:  ")
    
flavor = input("\nWhat flavor?:  ")
while len(flavor) == 0:
    flavor = input("\nCannot be left blank!, Enter a flavor:  ")
    
crustType = input("\nWhat style crust?:  ")
while len(crustType) == 0:
    crustType = input("\nCannot be left blank !!!  Enater a crust type.:  ")
    
    
quantity = input("\nHow many you want?   Enter a number value:  ")
while not quantity.isdigit():
    quantity = input("\nValue not recognized. Enter a numeric value:  ")
    
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














