from unittest import TestCase
import os

import Artstore
from Artstore import Artist, Artwork, ArtError
from db_config import test_database


# sadness and lack of working 

class TestArtstore(TestCase):

    def setUp(self):
        Artstore.create_test_artist_table()
        Artstore.create_test_artwork_table()

    def reset_tables(self):
        Artstore.drop_test_tables()



    def add_test_data(self):
        self.reset_tables()

        self.artist1 = ('bob', 'bob@boberson.com')
        self.artist2 = ('billy', 'billy@billyierson.com')
        self.artwork1 = ('blobalisa', 300, True,1)
        self.artwork2 = ('bong', 5000, False,2)


        self.bk1.save()
        self.bk2.save()
        self.bk3.save()


    def clear_bookstore(self):
        self.BS.delete_all_books()