d = {}
li = []

class Stock:
    def fruit_stock(self):
        try:
            fruit_name = input("Enter Fruit Name: ").strip()
            fruit_qty = int(input("Enter Fruit Qty (In Kg): "))
            fruit_price = int(input("Enter Fruit Price: "))

            d[fruit_name] = {"fruit_qty": fruit_qty, "fruit_price": fruit_price}
            print("\n Stock Added Successfully:")
            print(d)
            li.append(d.copy())
        except ValueError:
            print(" enter numeric values.")
        except Exception as e:
            print(f" Unexpected error: {e}")

class View(Stock):
    def fruit_view(self):
        if not d:
            print("No stock available.")
            return
        print("\n Current Fruit Stock:")
        for fruit, details in d.items():
            print(f"{fruit} :")
            for key, value in details.items():
                print(f"  {key} : {value}")

class Update(View):
    def fruit_update(self):
        try:
            fruit_name = input("Enter Fruit Name to Update: ").strip()
            if fruit_name not in d:
                print(" Fruit not found in stock.")
                return
            fruit_qty = int(input("Enter New Fruit Qty (In Kg): "))
            fruit_price = int(input("Enter New Fruit Price: "))

            d[fruit_name] = {"fruit_qty": fruit_qty, "fruit_price": fruit_price}
            print(" Stock Updated Successfully.")
        except ValueError:
            print(" Invalid input! Please enter numeric values.")
        except Exception as e:
            print(f" Unexpected error: {e}")

obj = Update()

menu = """
     WELCOME TO FRUIT MARKET 

    1) Manager
    2) Customer
"""

while True:
    try:
        print(menu)
        role = int(input("Select Your Role : "))
        if role == 1:
            while True:
                fruit_menu = """
                 Fruit Market Manager Menu

                1) Add Fruit Stock
                2) View Fruit Stock
                3) Update Fruit Stock
                4) Exit
                """
                print(fruit_menu)

                try:
                    choice = int(input("Enter Your Choice: "))
                    if choice == 1:
                        obj.fruit_stock()
                    elif choice == 2:
                        obj.fruit_view()
                    elif choice == 3:
                        obj.fruit_update()
                    elif choice == 4:
                        print("Thanks For Visit \n")
                        break
                    else:
                        print("Please select between 1 to 4.")
                except ValueError:
                    print("Please enter a valid number for choice.")
        elif role == 2:
            print("Custome Role Not Supported \n")
            break
        else:
            print("Invalid role selected.")
    except ValueError:
        print("Please enter a valid number.")