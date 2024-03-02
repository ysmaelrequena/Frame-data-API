#                                       A Fighting Game API so you can get the frame data of the characters and build your dream App!

The "FGPI" is, like its name indicates, is a compendium of frame data from different games, so that developers can fetch all the information and build tools for players looking for 
competitive knowledge of their game.

##                                       How did I build it?


#                                        The "Character_class" module

FGPI was built with Python in tandem with the FastAPI framework, which is equipped with several features that helped me streamline the creation process. Aside from that, 
I reutilized the Web Scraper from my last project: "The Street Fighter 6 Frame Data CLI Tool", but I adapted it to use a different approach this time that makes it easier 
to maintain and update in the long term: instead of just scraping and dropping everythin into a database, I followed the 'Builder' design pattern, and created a class which was 
initialized with four properties: two ("name" and "url") that are to be set up at the moment of calling the class to get the information to the database, and two ("htmltext" 
and "framedata") that are initialized as None because they're going to be mutated into the HTML of the web page and the character's frame data by the methods I wrote into the
class. This is all contained in the "Character_class" module that is inside the routers/SF6 directory of the project.

The three methods inside this "Character" class are the following:

```
set_htmltext
```

- Gets the HTML from the website it's scraping and it assigns it to the "htmltext" property of the "Character" class.

```
character_scrape
```

- This class contains the web scraper, it goes to the web page, in this case Supercombo wiki (for any character), and extracts the information, stores it into multiple dictionaries and
these are appended into a "character_framedata" dictionary, thus creating a dictionary that contains all the frame data for the character in an organized way that's easy to handle.

```
get_framedata
```

- Last but no least, this method runs the two methods described above and returns the dictionary with all the information needed.


  #                                        Storing the data

For the Database, I went with a SQL solution and the RDBMS I used was MySQL.

The database consists initially of a 'characters' table that contains every character and their ID in the system that will serve as our foreign key to
assign their respective moves to them. 

In the ```insert_data_db(move_t, table, character_id)``` function located in the 'character_table_creation' module

I created two modules called 'character_table_creation' and 'db_connection_generic', respectively.

- 'character_table_creation' contains three funtions:

```
character_class_definer(character_id)
```

This creates an instance of the 'Character' class described above, and separates the subdictionaries for every type of move for the insertion into the database in the next class.


```
insert_data_db(move_t, table, character_id)
```

This one connects to the database using the code imported from 'db_connection_generic' and loops through the dictionaries to insert everything in the database, after it finishes, it closes the
connection to the database.


```
main_data_insert_recursion(current_character_id, max_character_id)
```

This one, as its name indicates, is a recursive function that, once ran by the developer, it goes through all of the character IDs (defined in the database) and runs the function for each character
in their respective URL from the SuperComboWiki and finally, inserts everything into the different tables created for every type of move.

