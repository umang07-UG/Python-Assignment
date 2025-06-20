d={}
def fruit_stock():
    fruit_name=input("Enter Fruit Name: ")
    fruit_qty=int(input("Enter Fruit Qty (In Kg) : "))
    fruit_price=int(input("Enter Fruit Price : "))
    

    d[fruit_name]={"fruit_qty":fruit_qty,"fruit_price":fruit_price}
    print(d)
    li.append(d)


def fruit_view():
    
    for i,k in d.items():
        print(i," :")
        for t,j in k.items():
            print("  ",t,":",j)

def fruit_update():
    fruit_name=input("Enter Fruit Name: ")
    fruit_qty=int(input("Enter Fruit Qty (In Kg) : "))
    fruit_price=int(input("Enter Fruit Price : "))
    

    d[fruit_name]={"fruit_qty":fruit_qty,"fruit_price":fruit_price}
    


li=[]

menu = """

    WELCOME TO FRUIT MARKET

    1) Manager
    2) Customer

"""
#print(menu)
while True:
    print(menu)
    role=int(input("Select Your Role : "))
    while True:
        
        if role==1:
            
            fruit="""

            Fruit Market Manager

            1) Add Fruit Stock
            2) View Fruit Stock
            3) Update Fruit Stock
            4) Exit
        """
            
        print(fruit)

        choise=int(input("Enter Your Choise : "))

        if choise==1:
            fruit_stock()
        elif choise==2:
            fruit_view()
        elif choise==3:
            fruit_update()
        elif choise==4:
            print()
            break
        else:
            print("Invalid Choise")
