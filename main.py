import ui 
import Artstore 
from Artstore import Artist, Artwork

def main():
    Artstore.create_artist_table()
    Artstore.create_artwork_table()
    while True:
        print_menu()

        # what does the user want to do?
        # print menu
        task = input('Choose a task: ') 

        if task == '1':
            add_artist()
        elif task == '2':
            add_artwork()
        elif task == '3':
            search_by_artist()
        elif task == '4':
            search_by_artist_available()
        # elif task == '5':
        #     # change_availability()
        # elif task == '6':
        #     # delete_art()
        elif task.upper() == 'Q':
            print('Thanks. see you later!')
            break
        # etc... 

def print_menu():

    print('\n1: New Artist')
    print('2: Add new artwork')
    print('3: Search artwork by artist')
    print('4: Search available artworks by artist')
    print('5: Change art availability')
    print('6: Delete artwork')
    print('Q: Quit')

def add_artist():

    try:
        new_artist = ui.get_artist_data()

        Artstore.add_artist(new_artist)
    except Exception:
        print('Cannot add the same artist')

def add_artwork():
     
    artwork , artist = ui.get_artwork_data()

    artist_found = Artstore.search_for_artist(artist)

    try:
        if not artist_found:
            print('No artist with that name exists')
        else:
            new_artwork = Artwork(artist_found[0],artwork.artwork_name,artwork.price,artwork.availability)
            Artstore.add_new_artwork(new_artwork)
            print('Artwork successfully added')
    except Exception:
        print('sorry artwork already exists')

def search_by_artist():

    artist_name = ui.get_non_empty_string('Enter name of artist: ')

    artist_found = Artstore.search_for_artist(artist_name)

    if not artist_found:
        print('No artist with that name exists')
    else:
        artworks = Artstore.search_for_all_artwok(artist_found[0])
        ui.print_artworks(artworks)

def search_by_artist_available():

    artist_name = input('Enter name of artist')

    artist_found = Artstore.search_for_artist(artist_name)

    if not artist_found:
        print('No artist with that name exists')
    else:
        artworks = Artstore.search_for_all_artwok(artist_found[0])
        for art in artworks:
            if art[2] == 0:
                artworks.remove(art)
        
        ui.print_artworks(artworks)
    


       

if __name__ == "__main__":
    main()