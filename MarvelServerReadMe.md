# Connecting to MariaDB  
Navigate to the MariaDB\bin directory and enter the following in your shell to connect:  
.\mariadb -uroot -proot  

If you wish to use a username or password other than "root", enter it here, but be sure to update line 12 of MarvelServer.py to reflect the same info.  


# Creating the database and table structure  
To create the database, enter:  
create database marvel_crisis_protocol;  

To create the table structure, enter:  
create table characters(name varchar(255), threat int(11), health int(11), id int(11) auto_increment primary key, affiliation varchar(255));  


# REST Operations  

After opening MarvelServer.py and rest-client.rest in your code editor of choice, start running MarvelServer.py to connect to your database.  

<b>RUN THIS OPERATION FIRST:</b>    
POST http://localhost:5111/characters/bulk    
This will populate your characters table with the data necessary to properly utilize the other REST operations.     

 
GET http://localhost:5111/    
This is a landing page that returns a simple line of text.  


GET http://localhost:5111/characters    
This will return a list of all the data in the characters table.  


GET http://localhost:5111/characters/13    
This will return the data for the character with ID 13. Change the number in the query to select a character with a different ID.  


POST http://localhost:5111/characters    
This will create a new entry in the character table.   
This, by default, creates the character "Scream", but you may enter different data as needed.  
Note_1: the table is set to auto-increment character IDs. Should you need to reset that number (for instance, if you deleted an earlier character), enter:  
alter table characters auto_increment = 1;  
Note_2: When entering a character with multiple affiliations, use the following format in regard to the commas and spaces:  
"affiliation":"Brotherhood , Cabal"   


GET http://localhost:5111//characters/query?threat=3&health=5  
This will return a list of characters who match the criteria in the query parameters.   
By default, it will return all characters in the table who have 3 threat and 5 health.   
The query can be changed using the following parameters after "http://localhost:5111//characters/query?" and replacing 'value' with the data you wish to search for:  
name='value'  
threat='value'  
health='value'  
affiliation='value'  


DELETE http://localhost:5111/characters/13  
This will delete a character from the table that matches the ID number in the request.   
By default, it will delete the character with ID 13, but you may change it to any ID you wish.  
Note that by deleting a character, their ID will not be backfilled when creating a new character unless you reset the auto-increment value in your MariaDB instance with this command:  
alter table characters auto_increment = 1;  


PUT http://localhost:5111/characters/13  
This will update a character with new data based on the ID number used.  
By default, it will update whatever character has ID 13 to instead become the character "Cloak" and his associated data.   
The ID can be changed in the query to update a different character as needed.  
While you can update all of the columns in one entry as done in the default example, you may also choose to update only one or several at a time instead.  


