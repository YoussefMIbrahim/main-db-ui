import sqlite3
from db_config import database, test_database

#classes to hold both my artists and their works
class Artist:

    def __init__(self,name,email,id=None):
        
        self.name = name
        self.email = email
        self.id = id

class Artwork:

    def __init__(self,artistID,artwork_name,price,availability):

        self.artistID = artistID
        self.artwork_name = artwork_name
        self.price = price
        self.availability = availability


# creating artist table with a primary key 
def create_artist_table():


    with sqlite3.connect(database) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS artists(\
            artistId INTEGER PRIMARY KEY,\
            name TEXT UNIQUE, \
            email TEXT UNIQUE)")
    conn.close()

        
# creating artwork table with foriegn key connected to the primary from artist table
def create_artwork_table():
    with sqlite3.connect(database) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS artwork(\
            name TEXT UNIQUE, \
            price INTEGER,\
            available BOOLEAN,\
            workArtist INTEGER,\
            FOREIGN KEY(workArtist) REFERENCES astists(arstistId))")
    conn.close()

# using a prepared statement to add an artist and raising an error if they already exist
def add_artist(artist):

    sql = 'INSERT INTO artists (name , email) VALUES (?,?)'

    try:
        with sqlite3.connect(database) as con: 
            res = con.execute(sql,(artist.name,artist.email))
            new_id = res.lastrowid
            artist.id = new_id
    except sqlite3.IntegrityError as e:
        raise ArtError('Sorry aritst already exists in the database.') from e
    finally:
        con.close()

# Checking if artist is in the database and eiter returning them or false if they don't exist
def search_for_artist(name):

    find_artist_sql = 'SELECT * FROM artists WHERE UPPER(name) = UPPER(?)'


    con = sqlite3.connect(database)
    res = con.execute(find_artist_sql, (name,))
    artist = res.fetchone()

    con.close()

    if artist == None:
        return False
    else:
        return artist

## Checking if artwork is in the database and eiter returning them or false if they don't exist
def search_for_artwork(artwork_name):

    find_artwork_sql = 'SELECT * FROM artwork WHERE UPPER(name) = UPPER(?)'

    con = sqlite3.connect(database)
    res = con.execute(find_artwork_sql, (artwork_name,))
    artwork = res.fetchone()

    con.close()

    if artwork == None:
        return False
    else:
        return artwork


# adding a new artwork after making sure it doesn't exist
def add_new_artwork(artwork):

    add_artwork_sql = 'INSERT INTO artwork (name, price, available, workArtist) VALUES (?,?,?,?)'

    try:
        with sqlite3.connect(database) as con:
            con.execute(add_artwork_sql, (artwork.artwork_name,artwork.price, artwork.availability, artwork.artistID))
    except sqlite3.IntegrityError as e:
        raise ArtError('Sorry artwork already exists') from e
    finally:
        con.close()

# # getting artist id from main and gettting all thei artwork
def search_for_all_artwok(artistID):

    get_all_artwork_sql = 'SELECT * FROM artwork WHERE workArtist = ?'

    con = sqlite3.connect(database)
    res = con.execute(get_all_artwork_sql, (artistID,))

    artworks = []

    for r in res:
        artworks.append(r)
    con.close()

    return artworks

# updating the availability of an artwork and reaising an error if it was not found

def change_availability(availability, artwork_name):

    update_artwork_availability_sql = 'UPDATE artwork SET available = ? WHERE name = ?'

    with sqlite3.connect(database) as con:
        update = con.execute(update_artwork_availability_sql,(availability, artwork_name))
        rows = update.rowcount
    con.close()

    if rows == 0:
        raise ArtError(f'No artwork named {artwork_name} was found.')

# getting artowrk name and deleting it, raising an error if no rows were modified
def delete_artwork(artwork_name):

    delete_sql = 'DELETE FROM artwork WHERE name = ?'

    with sqlite3.connect(database) as con:
        delete = con.execute(delete_sql, (artwork_name,))
        rows = delete.rowcount
    con.close()

    if rows == 0:
        raise ArtError(f'No artowrk named {artwork_name} was found.')

        

# todo other DB interaction

class ArtError(Exception):
    pass



def create_test_artist_table():


    with sqlite3.connect(test_database) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS artists(\
            artistId INTEGER PRIMARY KEY,\
            name TEXT UNIQUE, \
            email TEXT UNIQUE)")
    conn.close()

        

def create_test_artwork_table():
    with sqlite3.connect(test_database) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS artwork(\
            name TEXT UNIQUE, \
            price INTEGER,\
            available BOOLEAN,\
            workArtist INTEGER,\
            FOREIGN KEY(workArtist) REFERENCES astists(arstistId))")
    conn.close()

def drop_test_tables():
    with sqlite3.connect(test_database) as con:
        con.execute('DROP TABLE IF EXISTS artists')
        con.execute('DROP TABLE IF EXISTS artwork')
    con.close