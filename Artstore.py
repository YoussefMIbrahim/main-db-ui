import sqlite3
from db_config import database




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



def create_artist_table():


    with sqlite3.connect(database) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS artists(\
            artistId INTEGER PRIMARY KEY,\
            name TEXT UNIQUE, \
            email TEXT UNIQUE)")
    conn.close()

        

def create_artwork_table():
    with sqlite3.connect(database) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS artwork(\
            name TEXT UNIQUE, \
            price INTEGER,\
            available BOOLEAN,\
            workArtist INTEGER,\
            FOREIGN KEY(workArtist) REFERENCES astists(arstistId))")
    conn.close()


def add_artist(artist):
    # todo 

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


def add_new_artwork(artwork):

    add_artwork_sql = 'INSERT INTO artwork (name, price, available, workArtist) VALUES (?,?,?,?)'

    try:
        with sqlite3.connect(database) as con:
            con.execute(add_artwork_sql, (artwork.artwork_name,artwork.price, artwork.availability, artwork.artistID))
    except sqlite3.IntegrityError as e:
        raise ArtError('Sorry artowkr already exists') from e
    finally:
        con.close()

def search_for_all_artwok(artistID):

    get_all_artwork_sql = 'SELECT * FROM artwork WHERE workArtist = ?'

    con = sqlite3.connect(database)
    res = con.execute(get_all_artwork_sql, (artistID,))

    artworks = []

    for r in res:
        artworks.append(r)
    con.close()

    return artworks

def change_availability(availability, artwork_name):

    update_artwork_availability= 'UPDATE artwork SET available = ? WHERE name = ?'

    with sqlite3.connect(database) as con:
        update = con.execute(update_artwork_availability,(availability, artwork_name))
        rows = update.rowcount
    con.close()

    if rows == 0:
        raise ArtError(f'No artwork named {artwork_name} was found.')

        

# todo other DB interaction

class ArtError(Exception):
    pass
