budget=int(input("Enter your budget:"))
Total_cost=0
grocery_list={250:"corn flour",100:"wheat",50:"xyz"}

while budget>0:
    print("1.Add an item")
    print("2.Exit")
    choice=input("Enter your choice:")

    if choice == "1":
        product=input("Enter product:")
        quantity=float(input("Enter quantity in kg:"))
        price=int(input("Enter price per kg:"))
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
    if item==budget:
        print("Amount left can you buy",grocery_list[item])
    else:
        pass