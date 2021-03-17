budget=int(input("Enter your budget:"))
Total_cost=0
grocery_list={}

while budget>0:
    print("1.Add an item")
    print("2.Exit")
    choice=input("Enter your choice:")

    if choice == "1":
        product=input("Enter product:")
        quantity=float(input("Enter quantity in kg:"))
        price=int(input("Enter price per kg:"))
        grocery_list[product]=price
        Total_cost=price*quantity
        budget=budget-Total_cost

        if budget==0 or budget<0:
            print("can't buy product beacause budget left is less")
        else:
            print("Amount left:", budget)
    elif choice=="2":
        break;

    else:
        print("Invalid input")

for item in grocery_list:
    if budget>= grocery_list[item]:
        print("Amount left can buy you",item)
    else:
        print("Thank You")
