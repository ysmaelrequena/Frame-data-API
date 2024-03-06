![Alt Text](https://github.com/ysmaelrequena/Fighting-game-API/blob/main/top10fighting-1660091625986.jpg)


#                                       A Fighting Game API so you can get the frame data of the characters and build your dream App!

The "FGPI" is, like its name indicates, is a compendium of frame data from different games, so that developers can fetch all the information and build tools for players looking for 
competitive knowledge of their game.

##                                       How did I build it?


###                                        The "Character_class" module

FGPI was built with Python in tandem with the FastAPI framework, which is equipped with several features that helped me streamline the creation process. Aside from that, 
I reutilized the Web Scraper from my last project: "The Street Fighter 6 Frame Data CLI Tool", but I adapted it to use a different approach this time that makes it easier 
to maintain and update in the long term: instead of just scraping and dropping everythin into a database, I followed the 'Builder' design pattern, and created a class which was 
initialized with four properties: two ("name" and "url") that are to be set up at the moment of calling the class to get the information to the database, and two ("htmltext" 
and "framedata") that are initialized as None because they're going to be mutated into the HTML of the web page and the character's frame data by the methods I wrote into the
class. This is all contained in the "Character_class" module that is inside the routers/SF6 directory of the project.

The three methods inside this "Character" class are the following:

```
set_htmltext(self)
```

- Gets the HTML from the website it's scraping and it assigns it to the "htmltext" property of the "Character" class.

```
character_scrape(self)
```

- This method contains the web scraper, it goes to the web page, in this case Supercombo wiki (for any character), and extracts the information, stores it into multiple dictionaries and
these are appended into a "character_framedata" dictionary, thus creating a dictionary that contains all the frame data for the character in an organized way that's easy to handle.

```
get_framedata(self)
```

- Last but no least, this method runs the two methods described above and returns the dictionary with all the information needed.



###                                        Storing the data

For the Database, I went with a SQL solution and the RDBMS I used was MySQL.

The database consists initially of a 'characters' table that contains every character and their ID in the system that will serve as our foreign key to
assign their respective moves to them. 

In the ```insert_data_db(move_t, table, character_id)``` function located in the 'character_table_creation' module, the tables for each type of move will be created when it runs for the first
character. In case the game gets updated, my preferred method of updating my database is dropping the tables in MySQL through a series of predetermined queries already stored in the 
'/MySQL_queries' directory of the project and running the ```main_data_insert_recursion(current_character_id, max_character_id)``` function located in the 'character_table_creation' module.

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
in their respective URL from the SuperComboWiki and finally, inserts everything into the different tables created for every type of move through our 'db_connection_generic'


-'db_connection_generic' contains two functions:

```
create_connection()
```

For this function to work, the developer should introduce the data where the parameters of their connection to their database and it'll let them create a conncetion to their database with MySQL, for example:

```
def create_connection():
    connection_params = {
        'host': 'here goes your connection instance',
        'user': 'here goes your username',
        'password': 'here goes your password',
        'database': 'fighting_game_api'
    }
```

Finally we have 

```
get_cursor(connection)
```

This will use the connection specified above to configure a cursor so the developer can execute the MySQL queries with Python.


###                                        Adquiring the data from the DB

I created a moduled called 'database_queries', in which the system queries the data for the character requested in the API whenever it gets a GET request. The module also includes a function which retrieves the
character list with their respective IDs.


###                                        Routing the data

After running the functions described above, the endpoints included in the 'sf6_endpoints' module are called by the 'main' module and their routed using FastAPI's integrated router system, whenever the user
does a GET request, the information is displayed.


##                                        Requirements

- Python 3.12.2 or newer.
- PIP.
- The project includes all its dependencies in the Run this command to install all the extra dependencies the 'requirements.txt' file.

 You can run this command in you CLI in the root directory of the project and Python will install all the dependencies needed:

```
pip install -r requirements.txt
```

##                                        Quick Start

```
git clone
https://github.com/ysmaelrequena/Fighting-game-API/
cd fighting_game_api
```

###                                     Run The Project Locally

1. Set up your database parameters in the 'db_connection_generic' module, then, using the query sheet in the 'MySQL_queries' folder, create the database with the queries:

```
CREATE DATABASE fighting_game_api;
USE fighting_game_api;
```


2. Inside the 'sf6/routers' directory run the following command in your CLI:

```
python character_table_creation.py
```

3. If you're using Uvicorn to run an instance of the API locally, then in the root directory of the project, run:

```
uvicorn main:app --reload
```
Then copy and paste the location that Uvicorn gives you into Postman or your web browser of choice and the API should work.


##                                        Endpoints

The following endpoints can be explored if you include a '/' and the name of the endpoint to the end of the URL:


Character List with their IDs:

```
yoururl/SF6/characters/
```

Character full movesets:

```
yoururl/SF6/characters/{EnterYourCharacterName}
```

Character move type list (example: normals, throws):

```
yoururl/SF6/characters/{EnterYourCharacterName}/movetype_list_name
```

Character list of moves separated by type:

```
yoururl/SF6/characters/{character_name}/{movetype}
```

##                                    Contribuing

If you'd like to contribute, please fork the repository and open a pull request to the main branch.











