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
            name TEXT UNIQUE NOT NULL, \
            price INTEGER NOT NULL,\
            available INTEGER NOT NULL,\
            workArtist INTEGER,\
            FOREIGN KEY(workArtist) REFERENCES astists(arstistId))")
    conn.close()


def add_artist(name, email):
    # todo 
    try:
        sql = 'INSERT INTO artists (name , email) VALUES (?,?)'
        with sqlite3.connect(database) as con: 
            con.execute(sql,(name,email))
        con.close()
    except sqlite3.IntegrityError as e:
        raise ArtError('Sorry aritst already exists in the database.') from e
    finally:
        con.close()


# todo other DB interaction

class ArtError(Exception):
    pass
