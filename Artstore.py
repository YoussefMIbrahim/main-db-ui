import sqlite3
from db_config import database




class Artist:

    def __init__(self,name,email,id=None):
        
        self.name = name
        self.email = email
        self.id = id

class Artwork:

    def __init__(self,artist,artwork,price,availability):

        self.artist = artist
        self.artwork = artwork
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
            available INTEGER,\
            workArtist INTEGER,\
            FOREIGN KEY(workArtist) REFERENCES astists(arstistId))")
    conn.close()


def add_artist(artist):
    # todo 

    sql = 'INSERT INTO artists (name , email) VALUES (?,?)'

    try:
        with sqlite3.connect(database) as con: 
            con.execute(sql,(artist.name,artist.email))
    except sqlite3.IntegrityError as e:
        raise ArtError('Sorry aritst already exists in the database.') from e
    finally:
        con.close()


# todo other DB interaction

class ArtError(Exception):
    pass
