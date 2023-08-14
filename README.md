# Portfolio  
Here you will find examples of Jeremy Hentschel's past projects.  

# Marvel Crisis Protocol Character Database and Web Server 
The "MarvelServer" files were constructed to utilize a Python Flask web server to interact with a MariaDB SQL database that holds a data set of the characters' attributes for the tabletop game Marvel Crisis Protocol.  This was devised to help keep track of the characters and their attributes in the game and track similarities between them.  

Be sure to take a look at MarvelServerReadMe.md for more instructions on how to utilize this program. 
You'll want to download "MarvelServer.py" and "MarvelServer_rest-client.rest" and have MariaDB installed to make full use of the program. 

# Store Inventory and Orders 
The "StoreInventory" files were constructed to make use of two separate CSV files (an inventory of a store's items organized by inventory numbers and a list of orders displaying who bought an item and for how much). This program was designed to read through the CSV files and parse them into Classes using Object Oriented Programming in order to manipulate and read their data in different ways.  

In StoreInventory_01, I have written a program that steps through the orders CSV file and pulls each item's inventory number from the inventory CSV file to include it as part of each order's data set. This was devised to help a store that implemented a numbered inventory system after they had already previously been selling items to customers using just the items' names.  

StoreyInventory_02 instead lists each item and its inventory number once and then includes a list of which customers bought each item and for how much. This was devised to help the store keep track of how much customers paid for items in order to make sure each customer was being treated fairly across multiple purchases.  

You'll want to download both "StoreInventory_01" and "StoreInventory_02" as well as the "inventory.csv" and "orders.csv" files to make full use of these programs. 
