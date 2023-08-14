orderfile = open("orders.csv","r")
inventoryfile = open("inventory.csv","r")

#Sets up classes for Order and InventoryItem
class Order:
    def __init__(self,customer,item_number, item_name, price):
        self.customer = customer
        self.item_number = item_number
        self.item_name = item_name
        self.price = price

class InventoryItem:
    def __init__(self,item_number,item_name):
        self.item_number = item_number
        self.item_name = item_name

# Loads instances of Inventory into a dictionary keyed by the item_number attribute
inventory = {}
for x in inventoryfile:
    parts = x.strip().split(",")
    inventory[int(parts[0])] = InventoryItem((int(parts[0])),parts[1])

# Loads instances of Orders into a list
orders = []
for x in orderfile:
    parts = x.strip().split(",")
    orders.append(Order(parts[0], int(parts[1]), inventory[int(parts[1])].item_name, int(parts[2])))

# Printout of inventory by item name and number comparing the prices different customers paid for the items.
for x in inventory:
    print(f"Item Number: {x}, Item Name: {inventory[x].item_name}")
    for y in orders:
        if x == y.item_number:
            print(f"{y.customer}:{y.price}")

orderfile.close()
inventoryfile.close()