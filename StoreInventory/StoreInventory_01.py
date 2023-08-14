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

# Loads instances of Inventory into a dictionary keyed by the item_number attribute. Use this example to access the instance values:
# print(inventory[11].item_name)
inventory = {}
for x in inventoryfile:
    parts = x.strip().split(",")
    inventory[int(parts[0])] = InventoryItem((int(parts[0])),parts[1])

# Loads instances of Orders into a list (uses the above dictionary to self-populate the Order item_name attribute by using dictionary's item_number key)
orders = []
for x in orderfile:
    parts = x.strip().split(",")
    orders.append(Order(parts[0], int(parts[1]), inventory[int(parts[1])].item_name, int(parts[2])))

# Print out of all the orders in the above list. 
for x in orders:
    print(f"Customer Name: {x.customer}, Item Number: {x.item_number}, Item Name: {x.item_name}, Price: ${x.price}")
    
orderfile.close()
inventoryfile.close()
