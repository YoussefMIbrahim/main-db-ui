import sqlite3

database = 'art.sqlite'


def create_artist_table():
    with sqlite3.connect(database) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS artists(\
            artistId INTEGER PRIMARY KEY,\
            name TEXT UNIQUE NOT NULL, \
            email TEXT UNIQUE NOT NULL)")
    conn.close()

def create_artwork_table():
    with sqlite3.connect(database) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS artwork(\
            FOREIGN KEY(workArtist) REFERENCES astists(arstistId),\
            name TEXT UNIQUE NOT NULL, \
            price INT NOT NULL,\
            available INT NOT NULL)")
    conn.close()


def add_artist(name, email):
    # todo 
    with sqlite3.connect(database) as con: 
        con.execute('')


# todo other DB interaction