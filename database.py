import sqlite3

database = 'art.sqlite'


def add_artist(name, email):
    # todo 
    with sqlite3.connect(database) as con: 
        con.execute('')


# todo other DB interaction